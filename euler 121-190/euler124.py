import math,time
start_time=time.time()
def divisors(n):
    d=[]

    if n==2:
        return [1,2]
    elif n==3:
        return [1,3]
    elif n==1:
        return [1]
    for r in range(1,int(n**0.5)+1):
        if n%r==0:
            d.append(r)
            if not((n/r) in d): 
                d.append(n/r)
    return sorted(d)
def is_prime(n):
    for r in range(2,int(n**0.5)+1):
        if n%r==0:
            return False
    return True
val=1
e=[]
for i in range(1,10**5 + 1):
    primes=divisors(i)
    for j in primes:
        if is_prime(j):
            val=j*val
    e.append([val,i])
    val=1
m=sorted(e)
print(m[10**4-1][1])
print("%s segundos ---------"%(time.time()-start_time))