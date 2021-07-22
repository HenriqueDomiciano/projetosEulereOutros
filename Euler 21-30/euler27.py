import math
def testeprimo(a):
    if a%2==0 and a != 2 :
        return False
    for d in range (2,math.ceil(math.fabs(a)**0.5)):
        n=a%d
        if n==0:
            return False 
        else:
            pass
    return True
def quadratic(a,b,n):
    return testeprimo((n*(n+a))+b)
contador,maximo_a,maximo_b,maximo=0,0,0,0
for a in range(-999,999,2):
    for b in range(-999,999,2):
        if testeprimo(b) and testeprimo(a+b+1):
            contador=0
            while quadratic(a,b,contador):
                contador=contador+1
                if contador > maximo :
                    maximo=contador
                    maximo_a=a
                    maximo_b=b
            
print(maximo,maximo_a*maximo_b)
 
