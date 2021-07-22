import math
def testeprimo(a):
    if a%2==0 and a != 2 :
        return False
    for d in range (2,math.ceil(math.fabs(a)**0.5)+1):
        n=a%d
        if n==0:
            return False 
        else:
            pass
    return True
primos_ate_mil = [i for i in range(11,1001) if testeprimo(i)]
def cicle_l(b):
    a= 1
    t = 0
    a = a*10 % b
    while(a!=1):
        a = a*10 % b
        t+=1
    return t+1 
res =[]
for i in primos_ate_mil:
    res.append([cicle_l(i),i])
print(max(res))

