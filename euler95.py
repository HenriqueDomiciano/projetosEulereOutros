def divisors(n):
    div=[]
    for a in range(2,int(n**0.5)+1):
        if n%a==0:
            div.append(int(a))
            div.append(int(n/a))
    b=(sum(div)+1)
    return b
temp=[]
final=[]
maximo=0
for a in range(10**4,4*10**4):
    m=a
    if temp==[]:
        temp.append(m)
    while not(divisors(temp[-1]) in temp) :
        u=divisors(temp[-1])
        temp.append(u)
        if (1 in temp) or temp[-1]>10**6 :
            temp=[]
            break
    else:
        if len(temp)>maximo and (divisors(temp[-1])==temp[0]):
            final=temp
            maximo=len(final) 
            temp=[]
        else:
            temp=[]
print(min(final))