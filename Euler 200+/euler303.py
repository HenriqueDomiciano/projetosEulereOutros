def f(n):
    if n==99:
        return 1122222222/99
    if n==999:
        return 111222222222222/999
    if n==9999:
        return 11112222222222222/9999
    a=1
    while True:
        c=list(str(n*a))
        for val in c:
            if int(val)<3:
                test=True 
            else:
                test=False
                break
        if test:
            return a
        a+=1
val=0
for r in range(20,31):
    print(f(r))
    val+=(f(r))
print(val)
