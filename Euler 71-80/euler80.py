#---------------------- chega perto mas nao acerta--------------------------------
from decimal import * 
getcontext().prec=101
def split(x):
    x=list(x)
    lista_1=[]
    for values in x : 
        lista_1.append(int(values))
    return sum(lista_1)
val=0
for r in range(0,101):
    if not(r**0.5%1==0):
        u=Decimal(r)**Decimal(0.5)
        u=str(u)[2:]
        print(len(u))
        val+=split(u)
print(val)