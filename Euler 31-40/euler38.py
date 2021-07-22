#naõ está terminado
import time
import numpy as np
import itertools
start_time=time.time()
value=[]
for s in itertools.permutations('123456789'):
    value.append((''.join(s)))
for m in value:
    if int(m[:4])%1==0:
        u=int(m[:4])
        if int(m[4:9])/2==u:
            last_value=m
print(last_value)
print('%s segundos'%(time.time()-start_time))

        
