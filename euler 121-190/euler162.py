#this is bad there must be other aproach
r=0
rel=0
m='0'
while len(m)<16:
    m=str(hex(r))[2:]
    if ('a' in m)  or ('0' in m) or ('1' in m):
        rel+=1
        
print((rel))
