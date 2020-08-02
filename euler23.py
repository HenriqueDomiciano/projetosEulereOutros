def abundant(n):
    value=[]
    for val in range(2,int(n**0.5)+1):
        if n%val==0:
            value.append(val)
            value.append(n/val)
    if (sum(value)+1)>n:
        return True
    else:
        return False
vector=[]
all_numbers=[]
tested=[]
for r in range(1,int(28146)):
    all_numbers.append(r)
    if abundant(r):
        vector.append(r)