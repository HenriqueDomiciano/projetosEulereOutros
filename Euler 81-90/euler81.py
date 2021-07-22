import numpy as np
matrix=[]
with open(r'C:\Users\Dell\Desktop\documentos\p081_matrix.txt','r') as f:
    content=f.readlines()
    for lines in content:
        reg=lines.split(',')
        for a in range(len(reg)):
            reg[a]=reg[a].rstrip("\n")
            reg[a]=int(reg[a])
        matrix.append((reg))
matrix=np.array(matrix)

for i in range(len(matrix)-2,-1,-1):
    matrix[len(matrix)-1,i]+=matrix[len(matrix)-1,i+1]
    matrix[i,len(matrix)-1]+=matrix[i+1,len(matrix)-1]
print(matrix)

for i in range(len(matrix)-2,-1,-1):
    for j in range(len(matrix[0])-2,-1,-1):
        matrix[i,j]+=min([matrix[i+1,j],matrix[i,j+1]])
print(matrix)
print(matrix[0][0])