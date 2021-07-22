import time 

start_time=time.time()

def calculate_area(x1,y1,x2,y2,x3,y3):
    return((x1*y2+x2*y3+x3*y1)-(x3*y2+y3*x1+x2*y1))
def calculate_area_origin(x1,y1,x2,y2):
    return x1*y2-(y1*x2)

with open(r'C:\Users\Dell\Desktop\documentos\p102_triangles.txt','r') as f:
    vector=f.readlines()

count=0
for value in vector:
    
    val=[]
    value=value.split(',')

    for values in value:
        val.append(int(values.rstrip('\n')))
    
    Area1=calculate_area(val[0],val[1],val[2],val[3],val[4],val[5])
    
    Area_AB=calculate_area_origin(val[0],val[1],val[2],val[3])
    
    Area_AC=calculate_area_origin(val[0],val[1],val[4],val[5])
    
    Area_BC=calculate_area_origin(val[2],val[3],val[4],val[5])
    
    if abs(Area1)==(abs(Area_AB)+abs(Area_AC)+abs(Area_BC)):
        count+=1
print(count)

print("%s seg"%(time.time()-start_time))