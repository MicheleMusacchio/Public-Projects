cut -f 2,8 instagram_posts.csv > instagram_description.csv
awk  -F'"' -vOFS='' '{if (length($2)>100) print $1}' instagram_description.csv > instagram_100.csv
head -10 instagram_100.csv



