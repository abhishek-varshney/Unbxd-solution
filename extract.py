import sys
import simplejson
from pprint import pprint

if __name__ == '__main__':
  if (len(sys.argv) != 5):
    print "usage : python extract.py [path to data.json] [path to query.json] [1/2 (Use case)] [Search query/Artist]"
    sys.exit(1)
  use_case="query" if int(sys.argv[3])==1 else "artist"  
  if sys.argv[3]=="1":
     l2 = simplejson.loads(open(sys.argv[2]).read())
  	 filter_out=filter(lambda x:x[use_case]==sys.argv[4],l2)
  	 del l2
  	 l1 = simplejson.loads(open(sys.argv[1]).read())
  if sys.argv[3]=="2":
  	l1 = simplejson.loads(open(sys.argv[1]).read())
  	filter_out=filter(lambda x:x[use_case]==sys.argv[4],l1)
  	del l1
  	l2 = simplejson.loads(open(sys.argv[2]).read())
  for row in filter_out: 
  	if sys.argv[3]=="1":
  		result_set=filter(lambda x: 1 if x["productId"]==row["productId"] else 0,l1)
  	if sys.argv[3]=="2":
  		result_set=filter(lambda x: 1 if x["productId"]==row["productId"] else 0,l2)
  	for row in result_set:
  		pprint(row)
