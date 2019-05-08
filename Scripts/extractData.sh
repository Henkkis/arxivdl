#!/bin/bash

source vars.sh

title_file="$parsed_data_folder/titles.temp"
category_file="$parsed_data_folder/categories.temp"
output_file="$parsed_data_folder/data.txt"

echo $title_file
echo $category_file
echo $output_file

rm -f $title_file
rm -f $category_file
rm -f $output_file

cd $raw_data_folder

for i in "${query_terms[@]}"; do
	grep -A 1 "<title>" --no-group-separator "$i.html"\
      	| grep -v  "<summary>"\
	| tr -d '\n'\
       	| sed 's/<title>/\'$'\n/g'\
	| sed 's/<\/title>//g'\
	| tail -n +2 >> $title_file\

	echo -e "" >> $title_file
done

for i in "${query_terms[@]}"; do
	grep "primary_category" "$i.html"\
       	|  grep -o -P '(?<=term\=").*(?=" scheme)'\
       	| cut -f1 -d "." >>$category_file
done


cd $parsed_data_folder

simple_category_file="categories.txt"
simple_title_file="titles.txt"
python "$script_folder/"simplify_categories.py $parsed_data_folder
python "$script_folder/"convert_title.py $parsed_data_folder
rm -f $title_file
rm -f $category_file

paste -d"\t" $simple_title_file $simple_category_file\
	| sort -R\
	| uniq  >$output_file

