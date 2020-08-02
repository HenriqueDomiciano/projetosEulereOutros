import time
start_time=time.time()
val=0
for r in range(1,22):
    for u in range(1,11):
        if len(str(u**r))==r:
            val+=1 
print(val)
print('-----%s segundos'%(time.time()-start_time))

