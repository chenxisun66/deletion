import numpy as np
from random import *
from findString import *

n = 20
m = 4
#filename = "result/"+str(n)+"/" + str(m)+ '_'+str(n)
filename = "result/" + str(m)+ '_'+str(n)
#filename = "result/"+str(n)+"/" + str(m)+ '_'+str(n)
ratios = np.zeros(2**(m-1))
with open(filename,'rb') as f:
    content = f.readlines()
    #print len(content)
    for i in range(2**(m-1)):
        substr = format(i, '0'+str(m)+'b')
        greedy_str = ''.join([c+c+c+c for c in substr])
        tmp = count(greedy_str,substr, len(greedy_str), len(substr))
        #print tmp
        #print content[i].split(',')[0]
        ratios[i] = tmp * 1.0 / int(content[i].split(',')[0])
        '''if ratios[i] < 0.5:
            print substr
            print greedy_str
            print tmp
            print content[i].split(',')[1]
            print int(content[i].split(',')[0])'''

#print ratios
#print ratios[::-1]
ratios = np.append(ratios,ratios[::-1])
print min(ratios)
'''for my1 in range(2**4):
    substr = format(my1, '05b')
    tmp = 0
    tmpstr = ""
    #print str(substr)+","
    for my2 in range(2**(9)):
        fullstr  = format(my2, '0'+str(10)+'b')
        #print(fullstr),
        #print(count(fullstr,substr, len(fullstr), len(substr)))
        if tmp < count(fullstr,substr, len(fullstr), len(substr)):
            tmp = count(fullstr,substr, len(fullstr), len(substr))
            tmpstr = fullstr
    print str(tmp)+","+tmpstr'''
