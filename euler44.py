def pentagon(n):
    return n*(3*n-1)/2
value=[]
for r in range(3000):
    value.append(pentagon(r))
for i in range(len(value)):
    for j in range(1,i):
        if ((value[i]+value[j]) in value):
            if (value[i]-value[j] in value):
                print(value[i]-value[j])
                break
            