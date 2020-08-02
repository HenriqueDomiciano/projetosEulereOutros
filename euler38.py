#naõ está terminado
import numpy as np
import itertools
value=[]
for s in itertools.permutations('123456789'):
    value.append((''.join(s)))
for m in value:
    if int(m[:4])%1==0:
        u=int(m[:4])
        if int(m[4:9])/2==u:
            print(u,'-----------------',m)


        
