import time
start_time=time.time()
powers=[]
for a in range(2,101):
    for b in range(2,101):
        if (a**b in powers):
            pass
        else :
            powers.append(a**b)
print(len(powers))
print('------%s segundos'%(start_time-time.time()))