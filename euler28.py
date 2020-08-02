import time 
start_time=time.time()
def sum_of_values(n):
    if n%2==0:
        return(n**2)+1+((n**2)-(n-1))
    else:
        return (n**2)+((n**2)-(n-1))

val=0
for r in range(2,1002):
    val=(sum_of_values(r))+val
print(val+1)
print('-----------%s segundos'%(start_time-time.time()))
