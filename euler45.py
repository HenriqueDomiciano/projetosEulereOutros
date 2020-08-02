def triangle(n):
    return (n*(n+1)/2)
def hexagonal(n):
    return n*(3*n-1)/2
def pentagonal(n):
    return n*(2*n-1)

pent=[]
hexa=[]
triang=[]

for i in range(1,100000):
    
    pent.append(pentagonal(i))
    hexa.append(hexagonal(i))
    triang.append(pentagonal(i))

for m in range(0,len(pent)):
    if (pent[m] in hexa) and (pent[m] in triang ):
        print(pent[m])
