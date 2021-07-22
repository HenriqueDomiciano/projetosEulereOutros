def is_bouncy(n):
    vect=[]
    m=-1
    count=0
    count1=0
    j=list(str(n))
    for val in j:
        vect.append(int(val))
    for v1 in range(len(vect)):
        if v1!=0:
            if vect[v1]>vect[v1-1]:
                count+=1
            if vect[v1]<vect[v1-1]:
                count1+=1
            if count1>=1 and count>=1:
                #print(count,'-------',count1)
                return False
        else:
            if vect[v1]<vect[v1+1]:
                count+=1
            if vect[v1]>vect[v1+1]:
                count1+=1
    return True
bon1=0
bon=0

for r in range(100,10**100):
    if is_bouncy(r):
        bon+=1
print(bon)