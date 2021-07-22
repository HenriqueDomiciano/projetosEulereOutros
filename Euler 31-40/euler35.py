import time
start_time=time.time()
def return_permuted(n):
    
    n=str(n)
    h=list((n)) 
    if (('0' in h) or ('2' in h) or ('4'in h) or ('6'in h) or ('8'in h) or ('5' in h)) and int(n)>10:
        return [] 
    u=n
    array=[]
    while not(int(n) in array):
        u=h.pop(0)
        h.append(u)
        m="".join(h)
        m=int(m)
        array.append(m)
    return array
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
primos=sieve(1000000)
circular_primes=[]
novo_circ=[]
for values in primos :
    u=return_permuted(values) 
    for m in u:
        if not(m in novo_circ):
            if (m in primos):
                circular_primes.append(m)
                if (circular_primes==u) and len(circular_primes)==len(u):
                    novo_circ=novo_circ+circular_primes
                    circular_primes=[]
                else:
                    pass
            else:
                circular_primes=[]
                break
        else:   
            break
print((len(novo_circ)))
print('---------%s------segundos'%((time.time()-start_time)))