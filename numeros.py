def multip():
    b=0
    c=0
    for a in range (0,1000):
        if a%3==0 or a%5==0:
            c=a+c    
    return c
print(multip())

    
