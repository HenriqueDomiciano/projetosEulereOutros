def is_permuteable(a,b):
    a=list(str(a))
    b=list(str(b))
    if len(a)==len(b):
       return sorted(a)==sorted(b)
    else:
        return False
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
primos1=sieve(2600)
primos2=sieve(4000)
minimo=1000000000
val=0
for r in primos1:
    for u in primos2:
        if is_permuteable((u-1)*(r-1),u*r):
            if u*r/((u-1)*(r-1))<=minimo:
                minimo=u*r/((u-1)*(r-1))
                val=u*r
print(val,'------------------',minimo)
