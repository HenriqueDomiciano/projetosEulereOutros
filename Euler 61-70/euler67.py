data=[]
with open(r'C:\Users\Dell\Desktop\p067_triangle.txt','r')as f:
    data=f.readlines()
new_data=[]
for v in data:
    new_data.append(v.rstrip())
for i in range(len(new_data)):
    new_data[i]=new_data[i].split(' ')
for i in range(len(new_data)):
    for j in range(len(new_data[i])):
        new_data[i][j]=int(new_data[i][j])
for i in range(len(new_data)-2,0,-1):
    for j in range(i+1):
        new_data[i][j]+=max([new_data[i+1][j+1],new_data[i+1][j]])
print(new_data[0][0]+max(new_data[1]))  
    