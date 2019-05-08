#!/bin/bash

source vars.sh
num_res=3000
cd $raw_data_folder

for i in "${query_terms[@]}"; do
    sleep 2
    wget "http://export.arxiv.org/api/query?search_query=all:$i&start=0&max_results=$num_res" -O $i.html
done
