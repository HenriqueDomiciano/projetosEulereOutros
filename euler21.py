def divisors(n):
    div=[]
    div1=[]
    for a in range(2,int(n**0.5)+1):
        if n%a==0:
            div.append(int(a))
            div.append(int(n/a))
    b=(sum(div)+1)
    if b==n:
        return False
    for a in range(2,int(b**0.5)+1):
        if b%a==0:
            div1.append(int(a))
            div1.append(int(b/a))
    c=sum(div1)+1
    if c==n:
        return True
    return False

a=0        
for r in range(1,10000):
    if divisors(r):
        a+=r
print(a)