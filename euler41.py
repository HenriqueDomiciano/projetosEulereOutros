import itertools
import math
def testeprimo(a):
    if a%2==0 and a != 2 :
        return False
    for d in range (2,math.floor(math.fabs(a)**0.5)):
        n=a%d
        if n==0:
            return False 
        else:
            pass
    return True
maximos=[]
valores=[]
for s in itertools.permutations('1234567'):
    value=(int(''.join(s)))
    valores.append(value)
for r in range(len(valores)):
    if testeprimo(valores[r]):
        maximos.append(valores[r])
print(max(maximos))
