import time
start_time=time.time() 
def split(x): 
    x=str(x)
    val=list(x)
    lista_1=[]
    for values in val : 
        lista_1.append(int(values))
    return sum(lista_1)
maximo=0
for a in range(1,101):
    for b in range(1,101):
        value=split(a**b)
        if value>maximo:
            maximo=value
print(maximo)
print('--------%s segundos'%(start_time-time.time()))