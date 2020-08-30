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
i=79
j=79
soma=[]
while i >0 and j>0:
    if (matrix[i][j-1]+matrix[i-1][j-1])<matrix[i-1][j-1]+matrix[i-1][j]:
        j-=1
        soma.append(matrix[i][j])
    else:
        i-=1
        soma.append(matrix[i][j])
print(i,'------------------',j)
print(sum(soma))
print(soma[-1])