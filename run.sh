#!/bin/bash
# This is a sample run file
# The script take a search query 'Less Than Jake' and prints all products related to the product id in search query. 3rd argument (1 here) indicates that it is search based on search query
echo "Getting desired results for search query 'Less Than Jake'"
echo ""
python extract.py data.json query.json 1 "Less Than Jake"
echo ""
echo "Getting desired results for artist 'Trial of the Bow'"
echo ""
# Here the script take an artist 'Trial of the Bow' and prints all search queries with which the product of particulat artist was associated. 3rd argument (2 here) indicates that it is search based on artist
python extract.py data.json query.json 2 "Trial of the Bow"
