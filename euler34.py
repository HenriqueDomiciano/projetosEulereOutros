# problema 34 e 74 é tudo muito lento  
import numpy as np
def split(x): 
    x=str(x)
    val=list(x)
    lista_1=[]
    for values in val : 
        lista_1.append(int(values))
    return(lista_1)
def factorial(x):
        n=1 
        for r in range(1,x+1):
            n=r*n
        return n
def sum_of_factorial(x):
    x=split(x)
    val=[]
    for n in range(len(x)): 
        val.append(factorial(x[n]))
    return sum(val)
def finding_values(r):
    x=0
    loop_values=[]
    loop_values.append(r)
    value=0
    while True: 
        value=sum_of_factorial(r)
        if not(value in loop_values) :
            loop_values.append(value)
            r=value
        else :
            return (loop_values)

x=1
u=0
while x<1000001:
    x=x+1
    if len(finding_values(x))==60:
        u+=1
        print(u,'----------',x)
