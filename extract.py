import sys
import csv
def load(path):
  ret=[]
	with open(path, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		for row in spamreader:
			ret.append(row)
	return ret

if __name__ == '__main__':
 
  if (len(sys.argv) != 5):
    print "usage : python extract.py [path to list 1] [path to list 2] [1/2 (Use case)] [Search query/Artist]"
    sys.exit(1)
  l1 = load (sys.argv[1])
  l2 = load (sys.argv[2])
  if sys.argv[3] == "1":
  	f1=filter(lambda x:x[0]==sys.argv[4],list(l2))
  	for row in list(f1): 
  		mapp=filter(lambda x: 1 if x[0]==row[1] else 0,list(l1)) 
  		for row in list(mapp):
  			print row
  if sys.argv[3] == "2":
  	f1=filter(lambda x:x[3]==sys.argv[4],list(l1))
  	for row in list(f1): 
  		mapp=filter(lambda x: 1 if x[1]==row[0] else 0,list(l2)) 
  		for row in list(mapp):
  			print row[0]
