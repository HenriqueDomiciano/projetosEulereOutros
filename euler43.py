import itertools
value=[]
for s in itertools.permutations('0123456789'):
    value.append((''.join(s)))
val=0
for r in range (len(value)):
    v=value[r]
    if int(v)%2==0:
        continue
    else: 
        if
         int(v[7:10])%17==0:
            if int (v[6:9])%13==0:
                if int(v[5:8])%11==0:
                    if int(v[4:7])%7==0:
                        if int(v[3:6])%5==0:
                            if int(v[2:5])%3==0:
                                if int(v[1:4])%2==0:
                                    val+=int(v)
print(val)