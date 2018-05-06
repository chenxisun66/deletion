from random import *
from findString import *
import itertools
import sys

# examples
'''substr = "1000101" # 00101
tmp = 0
for my_int in range(2**13,2**14):
    fullstr  = format(my_int, '014b')
    print(fullstr),
    print(count(fullstr,substr, len(fullstr), len(substr)))
    if tmp < count(fullstr,substr, len(fullstr), len(substr)):
        tmp = count(fullstr,substr, len(fullstr), len(substr))
print tmp'''

# experiment
m = 4


# length 4
#for j in k:
print "2**24"

#for my1 in range(2**3):
for my1 in range(5,6):
    substr = format(my1, '04b')
    tmp = 0
    tmpstr = ""
    print str(substr)+","
    for my2 in range(2**(23)):
        fullstr  = format(my2, '0'+str(24)+'b')
        #print(fullstr),
        #print(count(fullstr,substr, len(fullstr), len(substr)))
        if tmp < count(fullstr,substr, len(fullstr), len(substr)):
            tmp = count(fullstr,substr, len(fullstr), len(substr))
            tmpstr = fullstr
    print str(tmp)+","+tmpstr
