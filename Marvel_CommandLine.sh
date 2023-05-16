#MOST POPULAR PAIR OF HEROES
cat hero-network.csv | uniq -c | sort -nr | head -1
#applying "uniq -c" to count the occurrences and sorting it based on the occurrences number, then applying "head -1" we visualize the most popular one



##################################################
##################################################
#NUMBER OF COMICS PER HERO
cut -d, -f1 edges.csv | uniq -c > NUMBER_COMICS_PER_HERO.txt 
#considering only the first column and applying "uniq -c" to count the occurrences (i.e. the number of comics per hero, assuming  that there are no duplicates of same hero and same comic)
#storing the values in a .txt file

 
##################################################
##################################################
#AVERAGE NUMBER OF HEROES IN COMICS
num=$(cut -d, -f2 edges.csv| wc -l)
den=$(cut -d, -f2 edges.csv| uniq | wc -l)
(echo "scale=3; $num/$den" | bc)
#counting the total number of rows in the "comic" column 
#counting the total number of rows in the "comic" column where we have removed the duplicates using "uniq"
#dividing the total number of comics with occurrences, by the total number of comics without occurences
