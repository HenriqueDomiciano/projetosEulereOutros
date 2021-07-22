def collatz_function(n):
    list_1=[n]
    while not(list_1[-1]==1): 
        if (list_1[-1]%2)==0:
            list_1.append(list_1[-1]/2)
        else:
            list_1.append((3*list_1[-1])+1)
    return len(list_1)
maximo=0
max_r=0
for r in range(10000,1000000):
    m=collatz_function(r)
    if m>maximo:
        maximo=m
        max_r=r
print(max_r)