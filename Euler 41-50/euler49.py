import itertools
import time

start_time=time.time()

def sieve(p,n):
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
    for i in range(p, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime

primos=sieve(1001,10000)
value=[]
dif=0

for val in primos:
    for s in itertools.permutations(str(val)):
        m=int(''.join(s))
        
        if value==[]:
            value.append(m)
        
        if (m in primos) and (m!=val) and (not(m in value)) and (m-value[-1]==dif)  :
            value.append(m)
        
        if len(value)==1:
            dif=m-value[-1]
        
        if len(value)>2:
            print(value)
            break
    
    if len(value)>2:
        break
    
    else:
        value=[]

print("%s segundos"%(time.time()-start_time))