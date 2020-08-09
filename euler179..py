import time
start_time=time.time()
def divisors(n):
    b=0
    for a in range(2,int(n**0.5)+1):
        if n%a==0 :
            b+=2
    return b
u=1
#soma=102162
second_value=0
soma=0
for r in range(10,10001):
    actual_value=divisors(r)
    if actual_value==second_value:
        soma+=1
    second_value=actual_value
print(soma)
print('%s seg'%(time.time()-start_time))
