import itertools
def is_perfect_cube(x):
    return (x**(1/3))%1==0

value=[]
vector=[]
starting=5027
while len(vector)<5:
    fre=starting**3
    for s in itertools.permutations(str(fre)):
        value.append(int(''.join(s)))
    for a in value:
        if list(str(a)).count('0')>4:
            value=[]
            vector=[]
            break
        if is_perfect_cube(a) and (not(a in vector)):
            vector.append(a)
            print(vector)
    if len(vector)<5:
        value=[]
        vector=[]
        print(starting)
        starting+=1
    else:
        print(vector,starting)