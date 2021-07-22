import numpy as np
import math
val=np.zeros((1500001))
result=0
for m in range(2,int((1500000/2)**0.5)):
    for n in range(1,m):
        if (m+n)%2==1 and math.gcd(m,n)==1: 
            a=m**2-n**2
            b=m**2+n**2
            c=2*m*n
            p=a+b+c
            while p <= 1500000:
                val[p]+=1
                if (val[p] == 1):
                    result+=1
                if (val[p] == 2): 
                    result-=1
                p += a+b+c
print(result)