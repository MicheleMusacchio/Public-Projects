#!/bin/sh
echo " "
echo "How many places can be found in each country?"
echo " "

ENG=$(grep -c "England']" merged.tsv)
ITA=$(grep -c "Italy']" merged.tsv)
SPA=$(grep -c "Spain']" merged.tsv)
FRA=$(grep -c "France']" merged.tsv)
USA=$(grep -c "United States']" merged.tsv)
echo "Number of places in England: " $ENG
echo "Number of places in Italy: " $ITA
echo "Number of places in Spain: " $SPA
echo "Number of places in France: " $FRA
echo "Number of places in United States: " $USA


echo " "
echo "How many people, on average, have visited the places in each country?"
echo " "

TOT_VISIT_ENG=$(grep -i "England']" merged.tsv|awk -F'\t' '{ print $6 }'|awk '{s+=$1} END {print s}')
TOT_VISIT_ITA=$(grep -i "Italy']" merged.tsv|awk -F'\t' '{ print $6 }'|awk '{s+=$1} END {print s}')
TOT_VISIT_SPA=$(grep -i "Spain']" merged.tsv|awk -F'\t' '{ print $6 }'|awk '{s+=$1} END {print s}')
TOT_VISIT_FRA=$(grep -i "France']" merged.tsv|awk -F'\t' '{ print $6 }'|awk '{s+=$1} END {print s}')
TOT_VISIT_USA=$(grep -i "United States']" merged.tsv|awk -F'\t' '{ print $6 }'|awk '{s+=$1} END {print s}')
echo "Average visits in England: "$(bc <<<"scale=2; $TOT_VISIT_ENG / $ENG")
echo "Average visits in Italy: "$(bc <<<"scale=2; $TOT_VISIT_ITA / $ITA")
echo "Average visits in Spain: "$(bc <<<"scale=2; $TOT_VISIT_SPA / $SPA")
echo "Average visits in France: "$(bc <<<"scale=2; $TOT_VISIT_FRA / $FRA")
echo "Average visits in United States: "$(bc <<<"scale=2; $TOT_VISIT_USA / $USA")


echo " "
echo "How many people in total want to visit the places in each country?"
echo " "

WANT_VISIT_ENG=$(grep -i "England']" merged.tsv|awk -F'\t' '{ print $7 }'|awk '{s+=$1} END {print s}')
WANT_VISIT_ITA=$(grep -i "Italy']" merged.tsv|awk -F'\t' '{ print $7 }'|awk '{s+=$1} END {print s}')
WANT_VISIT_SPA=$(grep -i "Spain']" merged.tsv|awk -F'\t' '{ print $7 }'|awk '{s+=$1} END {print s}')
WANT_VISIT_FRA=$(grep -i "France']" merged.tsv|awk -F'\t' '{ print $7 }'|awk '{s+=$1} END {print s}')
WANT_VISIT_USA=$(grep -i "United States']" merged.tsv|awk -F'\t' '{ print $7 }'|awk '{s+=$1} END {print s}')
echo "Number of people want visit England: " $WANT_VISIT_ENG
echo "Number of people want visit Italy: " $WANT_VISIT_ITA
echo "Number of people want visit Spain: " $WANT_VISIT_SPA
echo "Number of people want visit France: " $WANT_VISIT_FRA
echo "Number of people want visit United States: " $WANT_VISIT_USA