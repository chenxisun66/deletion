import matplotlib.pyplot as plt
import pandas as pd



df = pd.read_csv('result/m_4.csv')


x = df['n']
y = df['ratio']
plt.plot(x, y, '--bo')
plt.xlabel('n')
plt.ylabel('ratio')
plt.title('m=4')
plt.ylim((0,1.1))
#plt.show()
plt.savefig('m_vary_n.eps',format='eps',dpi=1000)
