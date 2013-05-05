#!/bin/bash
# The script take a search query 'q1' and prints all products related to the product id in search query. 3rd argument (1 here) indicates that it is search based on search query
echo "Getting desired results for search query 'q1'"
echo ""
python extract.py list1.csv list2.csv 1 q1
echo ""
echo "Getting desired results for artist 'a1'"
echo ""
# Here the script take an artist 'a1' and prints all search queries with which the product of particulat artist was associated. 3rd argument (2 here) indicates that it is search based on artist
python extract.py list1.csv list2.csv 2 a1
