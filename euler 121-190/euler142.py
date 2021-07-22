def is_natural(x,y):
    if ((x-y)**0.5)%1==0:
        return True and (((x+y)**0.5)%1==0)
    else:
        return False
n=50000
for x in range(20001,n):
    for y in range(1,x):
        if is_natural(x,y):
            for z in range(1,y):
                if (is_natural(y,z) and is_natural(x,z)):
                    print(x,y,z)
        else:
            pass