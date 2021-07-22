import time
actual_time=time.time()
y_atual,y_anterior=0,21
x_atual,x_anterior=0,15
while y_atual<10**12:
    y_atual=(4*x_anterior)+(3*y_anterior)-3
    x_atual=(3*x_anterior)+(2*y_anterior)-2
    x_anterior=x_atual
    y_anterior=y_atual
print(x_atual,'--------',y_atual)
print('%s seg'%(time.time()-actual_time))