from random import *
from findString import *
import itertools
import sys

def expand(lst, n):
    lst = [[i]*n for i in lst]
    lst = list(itertools.chain.from_iterable(lst))
    return lst

# parameters

m = int(sys.argv[1])
k = int(sys.argv[2])
n = m * k
randBools =  lambda n: ''.join([str(randint(0,1)) for b in range(1,n+1)])

tmp = randBools(m)
a = ''.join(tmp)
b = ''.join(randBools(n))
c = ''.join(expand(tmp, k))
print('A binary vector of length %d: %s'%(m,a))
print('A randomly generated vector %s of length %d has %d \'%s \'' %(b,n,count(b,a, len(b), len(a)),a))
print('The guessed optimal vector %s of length %d has %d \'%s\''%(c,n,count(c,a, len(c), len(a)),a))
