import time
start_time=time.time()
vector=[]
new_content,new_content1=[],[]
with open(r'C:\Users\Dell\Desktop\p099_base_exp.txt','r') as f:
        content=f.readlines()
        for v in content:
            v= v.rstrip("\n")
            new_content.append(v)
for values in new_content:
    valor=values.split(',')
    new_content1.append(valor)
for values in new_content1:
    vector.append(int(values[0])**(int(values[1])/500000))
print(vector.index(max(vector))+1)
print('%s segundos'%(time.time()-start_time))