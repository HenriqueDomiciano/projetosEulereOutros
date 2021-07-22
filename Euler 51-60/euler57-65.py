import time
start_time=time.time()
a0=1
hn1=11
kn1=4
hn2=8
kn2=3
k=1
contador=2
for i in range(0,96):
    if contador<3:
        a0=1
    else:
        contador=0
        k+=1
        a0=k*2
    hn=a0*hn1+hn2
    kn=kn1*a0+kn2
    hn2=hn1
    kn2=kn1
    hn1=hn
    kn1=kn
    contador+=1
count=0
x=list(str(hn))
for val in x:
    count+=int(val)
print(count)
print("%s seg"%(time.time()-start_time))