#checking if is palindromic
def is_pali(x):
    x=str(x)
    return x==x[::-1]
soma=0
pali=[]
for r in range(0,int((10**8)**0.5)):
    for i in range(r,r+1000):
        soma+=i**2
        if is_pali(soma) and not( soma in pali) and soma!=r**2 and soma<10**8:
            pali.append(soma)
    soma=0
print(sum(pali)-1)

