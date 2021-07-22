n=50

def divisors(n):
    d=[]
    for r in range(1,int(n**0.5)+1):
        if n%r==0:
            d.append(r)
            d.append(int(n/r))
    return d

def factorial(x):
    count=1
    for m in range(x,1,-1):
        count*=m
    return count

def binomium(x,y):
    return (factorial(x)/(factorial(x-y)*factorial(y)))

numbers_in_pascal=[]

for x in range(1,n+1):
    for y in range(0,x+1):
        m=binomium(x,y)
        if not(m in numbers_in_pascal):
            numbers_in_pascal.append(m)

for val in numbers_in_pascal:
    divisores=divisors(val)
    for n in divisores:
        if (n**0.5)%1==0 and n!=1:
            numbers_in_pascal.pop(numbers_in_pascal.index(val))
            break

print(sum(numbers_in_pascal))