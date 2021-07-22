#did not undestand why
def split(x):
    val=[]
    x=str(x)
    x=list(x)
    for r in x:
        val.append(int(r))
    return sum(val)
a=0
r=1
value=[]
while a!=30:
    for m in range(1,40):
        j=r**m
        if split(j)==r and len(str(j))>1:
            value.append(j)
            a+=1
            break
    r+=1
print(sorted(value))