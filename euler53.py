import time
start_time=time.time()
def factorial(x):
        n=1 
        for r in range(1,x+1):
            n=r*n
        return n
val=0
for n in range(1,101):
    for r in range(1,n):
        res=factorial(n)/(factorial(r)*factorial(n-r))
        if res>10**6:
            val+=1
print(val)
print("%s segundos"%(time.time()-start_time))