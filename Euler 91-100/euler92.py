def split(x): 
    x=str(x)
    val=list(x)
    lista_1=[]
    for values in val : 
        lista_1.append(int(values)**2)
    return sum(lista_1)
temp,total=[],[]
val=0

for r in range(2,100001):
    u=r
    while u!=1:
        temp.append(u)
        if u in total:
            temp.pop(-1)
            total=total+temp
            temp=[]
            break
        if u==89:
            temp=[]
            break
        u=split(u)
    else:
        total=total+temp
        temp=[]

print(100000-len((total))+1)