def values(n):
    val=0
    c=(n**2)
    for r in range(1,n+1):
        if c%r==0:
            val+=1
    return val
a=1260
while values(a)<1000:
    a*=143#não sei se funciona para valores altos
    f=values(a)
    print(f)
print(a)