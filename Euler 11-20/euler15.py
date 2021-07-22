import numpy as np 

#construindo os numeros de herbert
def Latiffe_numbers(value):
    valor=np.ones((value+1,value+1))

    for i in range (len(valor)):
        for k in range(len(valor[0])):
            if k==0:
                valor[i,0]=1
            elif k>i:
                valor[i,k]=0
            else: 
                valor[i][k]=valor[i][k-1]+valor[i-1,k-1]+valor[i-1,k]
    return valor[i][k]
    #usando combinatoria o outro problema nao funcionou.
def combinatoria(val):
    paths=1
    for i in range(0,val):
        paths=paths*((2*val)-i)
        paths=paths/(i+1)
    return paths
print(combinatoria(20))
