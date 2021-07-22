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
dist=0
primos=sieve(1000000)
lastj=len(primos)
for i in range(len(primos)):
    for j in range(i+dist, lastj):
        sol = sum(primos[i:j])
        if sol < 1000000:
            if sol in primos:
                dist = j-i
                maior = sol
        else :
            lastj=j+1
            break
print(maior)
