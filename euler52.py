import time
start_timme=time.time()
def split(x): 
    x=str(x)
    val=list(x)
    lista_1=[]
    for values in val : 
        lista_1.append(values)
    return (lista_1)
r=120000
while True:
    a=r*2
    b=r*3
    c=a*2
    d=a*5
    e=b*2
    m=split(r)
    a=(split(a))
    b=(split(b))
    c=(split(c))
    d=(split(d))
    e=(split(e))
    z=True
    for t in range(len(m)):
        is_true=(m[t] in a) and (m[t] in b) and (m[t] in c) and (m[t] in d) and (m[t] in e)  
        z=is_true and z 
    if z:
        print(r)
        break
    r+=1
print("----------%s segundos"%(start_timme-time.time()))