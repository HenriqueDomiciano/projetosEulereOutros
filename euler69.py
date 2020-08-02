import time
from math import gcd
start_time=time.time()
def totient_function(n):
    val=0
    for p in range(1,n,2):
        if gcd(p,n)==1:
            val+=1
    return n/val
maximo=0
valor=1
n=6
a=2
while n<1000001:
    n=a*valor
    if totient_function(n)>maximo:
        maximo=totient_function(n)
        valor=n
        a=1
    a+=1
print(maximo,'-----------',valor)
print('%s segundos'%(time.time()-start_time))