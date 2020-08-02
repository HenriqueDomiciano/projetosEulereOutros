a= int(input("digite um valor"))
b=2
def primo(a,b):
    while b <= a-1 :
        n=a%b
        if (n==0):
            z=1
            b=a
        else :
            z=0
        b=b+1
    return z     
if primo(a,b)==1:
    print("n e primo")
else:
    print("e primo")
        
