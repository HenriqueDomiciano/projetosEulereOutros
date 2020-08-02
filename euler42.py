import time
start_time=time.time()
def function_score(a):
    new_func=[]
    a=list(a)
    for v in a:
        new_func.append(ord(v)-64)
    return sum(new_func)
new_content=[]
with open(r'C:\Users\Dell\Desktop\p042_words.txt','r') as f:
        content=f.read()
        content=content.split(',')
        for j in content :
            j=j.replace('"','')
            new_content.append(j)
triangular_numbers=[]
val=0
for n in range(0,1000):
    triangular_numbers.append(0.5*n*(n+1))
for w in new_content:
    l=function_score(w)
    if l in triangular_numbers:
        val+=1
print(val)
print('---------%a segundos'%(start_time-time.time()))