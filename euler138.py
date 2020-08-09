import time
import math
start_time=time.time()
x_1,x_ant=0,-1
y_1,y_ant=0,0
valx=[]
while len (valx)<13:
    x_1=(-9*x_ant)+(10*y_ant)-8
    y_1=(8*x_ant)-(9*y_ant)+8
    valx.append(math.fabs(x_1))
    x_ant=x_1
    y_ant=y_1
print(sum(valx)-1)
print("%s segundos"%(time.time()-start_time))