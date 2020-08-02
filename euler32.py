import itertools
value=[]
vector=[]
for s in itertools.permutations('123456789'):
    value.append((''.join(s)))
for m in value:
    a,b,c=int(m[:2]),int(m[2:5]),int(m[5:9])
    if a*b==c:
        if not(c in vector):
            vector.append(c)
for m in value:
    a,b,c=int(m[:1]),int(m[1:5]),int(m[5:9])
    if a*b==c:
        if not(c in vector):
            vector.append(c)
print(sum(vector))