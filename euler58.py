import math
import time
start_time=time.time()
def sum_of_values(n):
    if n%2==0:
        return(n**2)+1,((n**2)-(n-1))
    else:
        return 0,((n**2)-(n-1))
def testeprimo(a):
    if a%2==0 and a != 2 :
        return False
    for d in range (2,math.floor(math.fabs(a)**0.5)):
        n=a%d
        if n==0:
            return False 
        else:
            pass
    return True
n=2
numb_primo=0
relate=1
while relate>0.1:
    u,z=sum_of_values(n)
    #print(u,'-------',z)
    if testeprimo(u) or testeprimo(z):
        if testeprimo(u) and testeprimo(z):
            numb_primo+=2
        else:
            numb_primo+=1
    else :
        pass
    if n%2==0:
        relate=(numb_primo/(((n)*2)+1))
    else :
        relate=numb_primo/((n*2)-1)
    n=n+1    
print(n,'------------',relate)
print('--------%s segundos'%(start_time-time.time()))