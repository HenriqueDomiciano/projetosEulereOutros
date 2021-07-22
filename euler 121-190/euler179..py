'''
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
soma=0
second_value=0
soma=0
for r in range(1,10*10**6):
    actual_value=divisors(r)
    if actual_value==second_value:
        soma+=1
    second_value=actual_value
print(soma)
print('%s seg'%(time.time()-start_time))
'''
L = 10**7

n = [0]*(L)
for i in range(2, L//2):
    for j in range(i*2, L, i):
        n[j] += 1

print ("Consecutive divisors =", sum(n[i] == n[i - 1] for i in range(3, L)))