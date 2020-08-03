#this is bad there must be other aproach
r=0
rel=0
m='2'
while len(m)<8:
    m=str(hex(r))[2:]
    if ('a' in m)  or ('0' in m) or ('1' in m):
        rel+=1
    r+=1
print(hex(rel))
