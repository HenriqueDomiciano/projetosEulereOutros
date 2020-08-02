import math
def square_numbers(n):
    a=1
    u=0
    for r in range(1,n+1):
        u=r+u
    return u
print(square_numbers(5))
def find_divisors(n):
    counter=0
    for r in range(1,int(n**0.5)):
        if (n%r)==0: 
            counter=counter+1
    return counter*2
val=0
n=12000
while(val<500):
    n=n+1
    val=(find_divisors(square_numbers(n)))
print(square_numbers(n))
