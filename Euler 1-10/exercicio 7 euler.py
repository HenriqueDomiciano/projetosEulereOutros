import math
def testeprimo(a):
    if a%2==0 and a != 2 :
        return False
    for d in range (2,math.ceil(math.fabs(a)**0.5)):
        n=a%d
        if n==0:
            return False 
        else:
            pass
    return True
def contagem():
    c=1
    a=1
    while c<10001:
        a=a+2
        if testeprimo(a):
            c=c+1
    return a  
print(contagem())
print(testeprimo(100)
