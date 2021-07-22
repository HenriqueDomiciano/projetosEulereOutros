import math
limit=10**5
val=0
for a in range(1,limit//2):
    for b in range(1,a+1):
        for c in range(1,b+1):
            if (c+b)<a and a+b+c<limit and math.gcd(math.gcd(a,b),c)==1:
                val+=1
print(val)