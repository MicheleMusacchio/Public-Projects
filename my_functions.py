from collections import Counter
from statistics import mean

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd


## Functionality 1
def TOP_N(N,G_hero_net,edges_df):
    subnodes=set([el for el in edges_df.groupby('hero').count().sort_values(by=['comic'],ascending=False).head(N).index])
    return G_hero_net.subgraph(subnodes)

def number_of_collaborations_dict(graph_type,graph):
    if graph_type==2:
        warning_dict = ('Valid only for type 1')
        return warning_dict
    else:
        node_list = []
        degree_node_list = []
        for node in graph:
            node_list.append(node)
            degree_node_list.append(graph.degree(node))
        colab_dict = dict(zip(node_list, degree_node_list))
        return colab_dict
    
def number_of_hero_in_each_comic_dict(graph_type):
    if graph_type!=2:
        warning = ('number_of_hero_in_each_comic: Valid only for type 2')
        return warning
    else:
        attr=nx.get_node_attributes(G_edges_net,'type')
        List_comics=[i for i in G_edges_net.nodes if attr[i]=='comic']
        Degree_comics=[G_edges_net.degree(j) for j in List_comics]
        return dict(zip(List_comics,Degree_comics))
    
def degree_distribution(graph):
    deg = [graph.degree(n) for n in graph.nodes()]
    deg_count = Counter(deg)
    return deg_count

def degree_mean(graph):
    deg = [graph.degree(n) for n in graph.nodes()]
    return mean(deg)

def nodes_hubs(graph):
    deg = [graph.degree(n) for n in graph.nodes()]
    percentile = np.percentile(deg, 95)
    return [n for n in graph.nodes() if graph.degree(n) > percentile]

def graph_density(graph):
    nodes_count = graph.number_of_nodes()
    max_edges = nodes_count * (nodes_count - 1) / 2
    edges_count = graph.number_of_edges()
    density = edges_count/ max_edges
    return density

def number_of_nodes(graph_type,graph):
    if graph_type == 1 :
        return graph.number_of_nodes()
    elif graph_type == 2 :
        comic=0
        hero=0
        attr=nx.get_node_attributes(G_edges_net,'type')
        Attr_comic=[i for i in G_edges_net.nodes if str(attr[i])=='comic']
        Attr_hero=[i for i in G_edges_net.nodes if str(attr[i])=='hero']
        return [len(Attr_comic),len(Attr_hero)]
    else:
        return ('Wrong type number')
    
## Visualization 1
def Viz1_graph_info(num_nodes, dens, avg_degree, density, graph_type):
    graph_info = pd.DataFrame()
    if graph_type == 1:
        graph_info['Number of nodes'] = [num_nodes]
        graph_info['Density'] = [dens]
        graph_info['Avg Degree'] = [avg_degree]
        graph_info['Sparse or Dense'] = [density]
    else:
        graph_info['Number of comic nodes'] = [num_nodes[0]]
        graph_info['Number of hero nodes'] = [num_nodes[1]]
        graph_info['Density'] = [dens]
        graph_info['Avg Degree'] = [avg_degree]
        graph_info['Sparse or Dense'] = [density]
    return graph_info

def Viz1_hubs(hubs):
    graph_hubs = pd.DataFrame()
    graph_hubs['Hubs'] = [*hubs]
    return graph_hubs

## Functionality 2
damping_factor = 0.85

def compute_pagerank(graph, pagerank):
    for node in graph:
        rank = 1- damping_factor
        for neighbor in graph[node]:
            rank += damping_factor * pagerank[neighbor] / len(graph[neighbor])
            pagerank[node] = rank
    return pagerank

def page_rank_metric(graph):
    directed_graph = graph.to_directed()
    pagerank = {node: 1/len(directed_graph) for node in directed_graph}
    while True:
        prev_rank = pagerank.copy()
        pagerank = compute_pagerank(directed_graph, pagerank)
        if all(abs(prev_rank[node] - pagerank[node]) < 0.001 for node in pagerank):
            break
    return (pagerank)

def betweeness_metric(graph): #MAKE SURE TO CONSIDER ONLY A SUBGRAPH BECAUSE THIS ALGORITHM IN VERY SLOW
    betweeness = {n: 0 for n in graph.nodes()}
    for node in graph.nodes():
        for destin in graph.nodes():
            if destin!=node:
                paths = list(nx.all_shortest_paths(graph, node, destin))
                for key in paths:
                    for value in paths:
                        if key!=value:
                            for n in paths[(key, value)]:
                                betweeness[n] += 1 / len(paths[(key, value)])
    return betweeness

def closeness_metric(graph):
    closeness = {n: 0 for n in graph.nodes()}
    for node in graph.nodes():
        count=0
        for destin in graph.nodes():
            if destin!=node:
                count += len(list(nx.all_shortest_paths(graph, node, destin)))
        closeness[node]=(len(graph.nodes())-1)/count   
    return closeness

def degree_metric(graph):
    deg={n: 0 for n in graph.nodes()}
    for node in graph.nodes():
        deg[node]=graph.degree[node]/(len(graph.nodes())-1)
    return deg #IF YOU COMPARE IT WITH THE BUILT IN FUNCTION THERE IS A DIFFERENCE OF e-16 IN THE VALUES, BASICALLY ARE THE SAME

#Visualization 2

def Vis2_table_maker(metric, graph_output, node_output):
    res = 0
    for value in graph_output.values():
        res += value
    avg_metric = res / len(graph_output)
    Vis2_table = pd.DataFrame()
    Vis2_table['Requested centrality measure'] = [metric]
    Vis2_table['All nodes in network (avg)'] = [avg_metric]
    Vis2_table['Given node'] = [node_output]
    return Vis2_table

#Functionality 4

def min_cut(graph, heroA, heroB):
    min_cut = nx.minimum_edge_cut(graph, heroA, heroB)
    return (min_cut)

#Functionality 5

def edge_to_remove(graph):
  G_dict = nx.edge_betweenness_centrality(graph)
  edge = ()

  # extract the edge with highest edge betweenness centrality score
  for key, value in sorted(G_dict.items(), key=lambda item: item[1], reverse = True):
      edge = key
      break

  return edge

def girvan_newman(graph, n_communities):
    
	# find number of connected components
	sg = nx.connected_components(graph)
	sg_count = nx.number_connected_components(graph)
	count = 0
 
	while(sg_count < n_communities):
		graph.remove_edge(edge_to_remove(graph)[0], edge_to_remove(graph)[1])
		sg = nx.connected_components(graph)
		count += 1
		sg_count = nx.number_connected_components(graph)

	sg = list(nx.connected_components(graph))

	return (sg, count)

#Visualization 5

def table_of_communities(comm):
    toc = pd.DataFrame(columns=['Heroes in each community'])
    toc.style.set_properties(**{'text-align': 'center'}, subset='columns')
    for i in range(len(comm)):
        toc.loc[f'Community_{i+1}'] = [comm[i]]
    
    return toc



