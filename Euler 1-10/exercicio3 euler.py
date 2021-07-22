import math
def testeprimo(a):
    if a%2==0 and a != 2 :
        return False
    for d in range (2,a//2):
        n=a%d
        if n==0:
            return False 
        else:
            pass
    return True
def divisoresnumero(a):
    divisores=[]
    for d in range (1,int(a**0.5)+1,2):
        if a%d==0 and testeprimo(d):
            divisores.append(d)
    return max(divisores)
print(divisoresnumero(600851475143))
