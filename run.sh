#!/bin/bash
# The script take a search query '30f7594e-1d16-40c9-8a66-8dc641d65187' and prints all products related to the product id in search query. 3rd argument (1 here) indicates that it is search based on search query
echo "Getting desired results for search query '30f7594e-1d16-40c9-8a66-8dc641d65187'"
echo ""
python extract.py list1.csv list2.csv 1 30f7594e-1d16-40c9-8a66-8dc641d65187
echo ""
echo "Getting desired results for artist Dolly"
echo ""
# Here the script take an artist 'Dolly' and prints all search queries with which the product of particulat artist was associated. 3rd argument (2 here) indicates that it is search based on artist
python extract.py list1.csv list2.csv 2 Dolly
