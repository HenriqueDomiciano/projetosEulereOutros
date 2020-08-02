def sum_of_inverse(n):
    x=str(n)
    m=x[::-1]
    return int(x)+int(m)
    
def is_tyrrel(n):
    val=0
    r=0
    while r<51 :
        n=sum_of_inverse(n)
        if str(n)==str(n)[::-1]:
            return False
        r+=1
    else:
        return True
val=0
for r in range(1,10001):
    
    if is_tyrrel(r):
        val+=1
print(val)
