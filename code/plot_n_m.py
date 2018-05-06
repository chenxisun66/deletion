import matplotlib.pyplot as plt
import pandas as pd



df = pd.read_csv('result/vary_m.csv')



fig,ax = plt.subplots()

for n in list(set(df['n'])):
#for n in [12,15,18]:
#for n in [8,12,16,20]:
#for n in [10,15,20]:
    ax.plot(df[df.n==n].m,df[df.n==n].ratio,label=n,marker='s',linestyle = '--')

ax.set_xlabel("m")
ax.set_ylabel("ratio")
ax.legend(loc='best')
plt.title('varying m')
plt.ylim((0,1.1))
plt.savefig('n_vary_m.eps',format='eps',dpi=1000)
