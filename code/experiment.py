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


print "2**",str(n)

for my1 in range(2**(m-1)):
    substr = format(my1, '0'+str(m)+'b')
    tmp = 0
    tmpstr = ""
    for my2 in range(2**(n-1)):
        fullstr  = format(my2, '0'+str(n-1)+'b')
        #print(fullstr),
        #print(count(fullstr,substr, len(fullstr), len(substr)))
        if tmp < count(fullstr,substr, len(fullstr), len(substr)):
            tmp = count(fullstr,substr, len(fullstr), len(substr))
            tmpstr = fullstr
    print tmpstr
    print str(tmp)+","+tmpstr
