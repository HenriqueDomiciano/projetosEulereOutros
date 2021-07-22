def split(x): 
    x=str(x)
    val=list(x)
    lista_1=[]
    for values in val : 
        lista_1.append(int(values))
    return(lista_1)
maximo=0
for a in range(100,1000):
    for b in range(100,1000):
        c=split(a*b)
        if len(c)%2==0:
            if c[0]==c[-1] and c[1]==c[-2] and c[2]==c[-3]:
                value=a*b
                if value>maximo:
                    maximo=value  
print(maximo)
