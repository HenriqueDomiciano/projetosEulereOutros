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
def is_truncable(n,lista):
    m=str(n)
    u=str(n)
    while len(m)!=0:
        if (int(m) in lista) and (int(u) in lista):
            m=m[:-1]
            u=u[1:]
        else:
            return 0
    return int(n)


value=sieve(1000000)
valor=0
for val in value:
    a=(is_truncable(val,value))
    valor+=a
print(valor-2-3-5-7)
print('%s segundos'%(time.time()-start_time))