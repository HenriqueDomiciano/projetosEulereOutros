val=[]
for r in range(1,10):
    val.append(str(r))
def is_pandigital(d,val):
    t=str(d)
    if  (all(item in list(t[:9]) for item in val)) and (all(item in list(t[-9:]) for item in val)):
        return False
    return True
def fibonacci():
    fib1=1
    fib2=1
    d=0
    c=2
    while is_pandigital(d,val) :
        d=fib1+fib2
        fib1=fib2
        fib2=d
        c+=1
    return c
print(fibonacci())
# muito demoraddo mas funciona