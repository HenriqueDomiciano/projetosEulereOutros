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
def create_composite(n,lista):
    val=[]
    for r in range(3,n,2):
        if not(r in lista):
            val.append(r)
    return val

primos=sieve(10000)
primos.remove(2)
composite=create_composite(10000,primos)
valy=[]
for val in primos:
    for r in range(1,100):
        gold=val+(2*(r**2))
        valy.append(gold)
for val in composite :
    if not(val in valy):
        print(val)


