def split(x): 
    x=str(x)
    val=list(x)
    lista_1=[]
    for values in val : 
        lista_1.append(int(values))
    return(lista_1)
def fibon(n):
    fib,b,contador=1,1,2
    val=1
    while contador<n:

        fib=b+fib
        b=val
        val=fib
        
        contador=contador+1
    return val
a=1
while(len(split(fibon(a))))<1000:
    a=a+1
print(a)

