me=0
a=0
while a<1000:
    if a%10==0:
        print(a)
        pass
    else:
        val=a**a
        me=val+me
    a=a+1
print(me%(10**10))
