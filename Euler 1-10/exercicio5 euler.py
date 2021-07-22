def divisivel(a):
    c=0
    if a%2 !=0 :
        return False
    for b in range (20,10,-1):
        n=a%b  
        if n==0:
            pass 
        else :
            return False
    return True
def numeros():
    a=2520
    valor=False
    while not(valor):
        a=a+2
        valor=divisivel(a)
    return a
        
print(numeros())        
        #nao funciona fatores primos funcinam
