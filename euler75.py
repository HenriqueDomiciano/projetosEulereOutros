import numpy as np
import math
val=np.zeros((1500000))
for m in range(2,1500000):
    for n in range(1,m):
        if (m+n)%2==0 and math.gcd(m,n)==1: 
            d=m**2-n**2
            e=m**2+n**2
            f=2*m*n
            c=d+e+f
            if c<=1500000:
                val[int(c)]+=1
print(len(np.where(val==1)[0]))