import itertools
value=[]
for s in itertools.permutations('0123456789'):
    value.append(int(''.join(s)))
value=sorted(value)
print(value[999999]) 
    