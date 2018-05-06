from random import *
from findString import *
import itertools
import sys


m = 4
n = 32

# length 4
#for j in k:
print "2**"+str(n)

substr = format(m+1, '04b')
tmp = 0
tmpstr = ""
print str(substr)

for my2 in range(2**(n-12)):
    fullstr_mid  = format(my2, '0'+str(n-12)+'b')
    fullstr = '000000'+fullstr_mid+'111111'
    #print(fullstr),
    #print(count(fullstr,substr, len(fullstr), len(substr)))
    if tmp < count(fullstr,substr, len(fullstr), len(substr)):
        tmp = count(fullstr,substr, len(fullstr), len(substr))
        tmpstr = fullstr
print str(tmp)+","+tmpstr
