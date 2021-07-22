#thanks Mathblog 
import numpy as np 
targ=100
valu=[]
valu=np.zeros(targ+1)
valu[0]=1
for i in range(1,targ+1):
    for j in range(i,targ+1):
        valu[j]+=valu[j-i]
print(valu[-1])
