import math
lista=[]
def values(n):
    val=0

    for r in range(1,round(n**0.5)+1):
        if math.gcd(n,r)==1:
            val+=1
    if (n!=2) and (n!=3):
        return 2*val
    elif n==2 :
        return 1
    elif n==3:
        return 2
val=0

for r in range(2,112):
    val=val+values(r)
print(val)

'''
def number_of_fractions():
    val=0
    for d in range(2,1000001):
        for n in range(1,d):
            val=n/d
            if not(val in lista):
                lista.append(val)
    return len(lista)
print(number_of_fractions())
'''