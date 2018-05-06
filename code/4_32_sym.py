from random import *
from findString import *
import itertools
import sys

assert len(sys.argv)==5, "not enough parameters! need to provide m,n"
print "input m:", sys.argv[1]
print "input n:", sys.argv[2]
print "input skip:", sys.argv[3]

'''m = 4
n = 28
skip = 4'''

m = int(sys.argv[1])
n = int(sys.argv[2])
skip = int(sys.argv[3])
write = int(sys.argv[4])

# length 4
#for j in k:
print "2**"+str(n)

substr = format(m+1, '04b')
tmp = 0
tmpstr = ""
print str(substr)
size = n/2-skip

for my2 in range(2**size):
    fullstr_mid_front  = format(my2, '0'+str(size)+'b')
    fullstr_half_front = '0'*skip+fullstr_mid_front
    fullstr_half_back = ''.join('1' if x=='0' else '0' for x in fullstr_half_front[::-1])
    fullstr = fullstr_half_front + fullstr_half_back
    '''print(fullstr)
    print(len(fullstr))
    break'''
    #print(count(fullstr,substr, len(fullstr), len(substr)))
    if tmp < count(fullstr,substr, len(fullstr), len(substr)):
        tmp = count(fullstr,substr, len(fullstr), len(substr))
        tmpstr = fullstr
record1= str(n)+','+ str(tmp)+","+tmpstr+'\n'
record2= str(n)+','+ str(1.0 * (n/m)**4 / tmp)+","+tmpstr+'\n'
print record1
print record2
if write==1:
    with open("result/4_20+", "a") as myfile:
        myfile.write(record1)

    with open("result/m_4.csv", "a") as myfile1:
        myfile1.write(record2)
