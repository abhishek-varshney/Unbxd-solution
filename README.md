Unbxd-solution
==============

The problem statement
======================

You have 2 lists of key-value pairs that you can query. Here are the details:
1st list: 1 million unique rows which are unique products that an eCommerce site is currently selling on their site.
Here are the list of attributes per product:

    productId
    productName
    genre
    artist

2nd list: It is a list of 10 million records. Each record has 2 items in them. The first item is a search query and tied to it is the second item - productID of the product that the user clicked, after she searched the query on the eCommerce site. This is the data that eCommerce site has seen in 1 day.
Here is the list of attributes per record:

    query
    productId
    timestamp


What you need to do:
You need to design a system which can hold the above mentioned data using data structures which are appropriate to support querying the data with the following use-cases:

    Given a search query, present a list of all products that were clicked with all the product attributes.
    Given an artist, find all the search queries which resulted in users clicking on product with the particular artist.


The solution
============

The problem is solved using map-filter-reduce paradigm in python. Although, the actual implementation did not require more than just a couple of filters. The data structure chosen here to store the contents of both the files is list. Dictionary could have been better (??).
The run bash script is included in the repos. There can be better solutions to the problem indeed !

The usage
=========

python extract.py [path of data.json] [path of query.json] [1/2 (query/artist)(based on desired use case)] [Query/Artist]

A sample run for both the use cases is given in run.sh file. Don't forget to chmod it to 777 before executing!

Note - Ignore if you are not from Unbxd Team
============================================

There is format error in the query.json provided. There are occurences of double comma like

{"query": "Lock and", "timestamp": "2012-12-28T00:00:00.045000+00:00", "productId": 322506},,{"query": "Velvet Crush", "timestamp": "2012-12-28T00:00:00.045000+00:00", "productId": 134363}

This double-comma is 130405'th character. There are many occurences of similar type. I formatted it through:

tr -s ',' < query.json > query.json.mod

mv query.json.mod query.json

