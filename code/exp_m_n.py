from random import *
from findString import *
import itertools
import sys


# experiment
assert len(sys.argv)==3, "not enough parameters! need to provide m,n"
print "input m:", sys.argv[1]
print "input n:", sys.argv[2]

m = int(sys.argv[1])
n = int(sys.argv[2])

# find num of occurance of substr in the all possible full string
# and save result to file
with open('result/'+str(n)+'/'+str(m)+'_'+str(n),'wb') as f:
    for my1 in range(2**(m-1)):
        substr = format(my1, '0'+str(m)+'b')
        tmp = 0
        tmpstr = ""
        for my2 in range(2**(n-1)):
            fullstr  = format(my2, '0'+str(n)+'b')
            if tmp < count(fullstr,substr, len(fullstr), len(substr)):
                tmp = count(fullstr,substr, len(fullstr), len(substr))
                tmpstr = fullstr
        print str(tmp)+","+tmpstr
        f.write(str(tmp)+","+tmpstr+'\n')
