import time 
start_time=time.time()
def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated
    for i in range(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime
def prime_factors(n,primos):
    a=primos[0]
    z=0
    factors=[]
    while n!=1 or a<n:
        if n%a==0 and n!=1:
            n=n/a
            factors.append(a)
        else:
            z+=1
            a=primos[z]
    factors= list(dict.fromkeys(factors))
    return factors
primos=sieve(400000)
values=[]
for m in range(1000,300000):
    if len(prime_factors(m,primos))==4:
        values.append(m)
        if len(values)==4:
            break
    else:
        values=[]
print(values)
print("%s segundos"%(time.time()-start_time))