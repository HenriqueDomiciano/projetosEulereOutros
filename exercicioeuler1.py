val=0
for r in range (1,1000):
    if r%3==0 or r%5==0: 
        val=r+val
print(val)