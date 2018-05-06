from random import *
from findString import *
import itertools
import sys



# experiment

assert len(sys.argv)==4, "not enough parameters! need to provide substr, n and skip"
print "input substr:", sys.argv[1]
print "input n:", sys.argv[2]
print "skip:",sys.argv[3]

substr = sys.argv[1]
n = int(sys.argv[2])
skip = int(sys.argv[3])
size = n-skip*2
m = len(substr)

tmp = 0
tmpstr = ""
for my_int in range(2** size):
    fullstr_mid  = format(my_int, '0'+str(size)+'b')
    fullstr = substr[0]*skip+ fullstr_mid + substr[-1]*skip

    if tmp < count(fullstr,substr, len(fullstr), len(substr)):
        tmp = count(fullstr,substr, len(fullstr), len(substr))
        tmpstr = fullstr

greedy_str = ''.join([c*(n/m) for c in substr])
tmp1 = count(greedy_str,substr, len(greedy_str), len(substr))
record= str(n)+','+ str(tmp)+","+tmpstr+","+greedy_str+","+str(1.0 * tmp1 / tmp)+'\n'
print record
