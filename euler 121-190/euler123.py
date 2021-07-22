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
for r in range(len(primos)):
    m=(((primos[r]+1)**r+1)+((primos[r]-1)**r+1))%primos[r]**2
    if m>10**10:
        print(r+1)
        break