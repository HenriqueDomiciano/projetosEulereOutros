import time
start_time=time.time_ns()
x1=5
y1=4
p=0
total=16
while p<10**9:
    xn=x1
    x1=(x1*7)+(8*y1)-2
    y1=(6*xn)+(7*y1)-2
    p=3*x1+1
    total+=p
total=total-p
x1=1
y1=1
p=0
while p<10**9:
    xn=x1
    x1=(x1*7)+(8*y1)+2
    y1=(6*xn)+(7*y1)+2
    p=3*x1-1
    total+=p
print(total-p)
print("%s seconds"%(int(time.time_ns()-start_time)/10**9))