import time
start_time=time.time()
def has_same_digit(a,b):
    m=list(str(a))
    n=list(str(b))
    if ('0' in m) or ('0' in n):
        return False
    for val in m:
        if (val in n) and (val !=0 ):
            try:
                m.remove(val)
                n.remove(val)
                m=int(''.join(m))
                n=int(''.join(n))
                if m/n == a/b:
                    return True
            except:
                return False
    return False
val=1
for b in range(10,100):
    for a in range(10,b):
        if has_same_digit(a,b):
            print(a,'/',b)
print('%s seg'%(time.time()-start_time))