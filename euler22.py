import time
start_time=time.time()
def function_score(a):
    new_func=[]
    a=list(a)
    for v in a:
        new_func.append(ord(v)-64)
    return sum(new_func)
new_content=[]
new_content_2=[]
new_content_3=[]
with open(r'C:\Users\Dell\Desktop\p022_names.txt','r') as f:
        content=f.read()
        content=content.split(',')
        for j in content :
            j=j.replace('"','')
            new_content.append(j)
new_content=sorted(new_content)
for i in new_content:
    new_content_2.append(function_score(i))
for i in range(0,len(new_content_2)):
    o=i+1
    new_content_3.append(new_content_2[i]*o)
print(sum(new_content_3))
print("----%s segundos"%(start_time-time.time()))


    