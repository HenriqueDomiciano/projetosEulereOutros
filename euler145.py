def split(x):
    if x%10==0:
        return False
    if int(str(x)[-1])%2!=0 and int(str(x)[0])%2!=0:
        return False
    elif int(str(x)[-1])%2==0 and int(str(x)[0])%2==0:
        return False
    else:    
        m=int(str(x)[::-1])
        u=list(str(x+m))
        for values in u :
            if int(values)%2==0:
                return False
    return True
val=[]
for r in range(10,50*(10**6)):
    if split(r) and (not(r in val)):
      val.append(r)
      val.append(int(str(r)[::-1]))  
print(len(val))