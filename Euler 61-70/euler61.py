def split(n):
    i=list(str(n))
    return i
def last_in_first(n,m):
    if n==m:
        return False
    a=(str(n)[2:])
    b=(str(m)[:2])
    if a==b:
        return True
    return False

def create_lists():
    square=[]
    triangle=[]
    octa=[]
    hexag=[]
    pent=[]
    hept=[]
    r=0
    while len(split(int(r*(r+1)/2)))<=4:
        if len(split(int(r**2)))>3:
            square.append(int(r**2))
            if (len(split(square[-1])))>=5:
                square.pop(-1)
        if len(split(int(r*(r+1)/2)))>3:
            triangle.append(int(r*(r+1)/2))
            if len(split(triangle[-1]))>=5:
                triangle.pop(-1)
        if len(split(int(r*(3*r-1)/2)))>3:
            pent.append(int(r*(3*r-1)/2))
            if len(split(pent[-1]))>=5:
                pent.pop(-1)
        if len(split(int(r*(2*r-1))))>3:
            hexag.append(int(r*(2*r-1)))
            if len(split(hexag[-1]))>=5:
                hexag.pop(-1)
        if len(split(int(r*(5*r-3)/2)))>3:
            hept.append(int(r*(5*r-3)/2))
            if len(split(hept[-1]))>=5:
                hept.pop(-1)
        if len(split(int(r*(3*r-2))))>3:
            octa.append(int(r*(3*r-2)))
            if len(split(octa[-1]))>=5:
                octa.pop(-1)
        r=r+1
    return triangle,square,pent,hexag,hept,octa
triangle,quadrado,pentagono,hexagono,eptagono,octogono=create_lists()

vector1=triangle
vector2=quadrado
vector3=pentagono
vector4=hexagono
vector5=eptagono
vector6=octogono
vector=vector1+vector2+vector3+vector4+vector5+vector6
value=[]
li=[0,0,0,0,0,0]
for val in vector:
    for val2 in vector:
        if last_in_first(val,val2) :
            for val3 in vector:
                if last_in_first(val2,val3):
                    for val4 in vector:
                        if last_in_first(val3,val4):
                            for val5 in vector:
                                if last_in_first(val4,val5):
                                    for val6 in vector :
                                        if last_in_first(val5,val6) and last_in_first(val6,val) and (val6 in vector6) :
                                            last=[val,val2,val3,val4,val5,val6]
                                            li=[0,0,0,0,0,0]
                                            for u in range(0,len(last)):
                                                if last[u] in vector1:
                                                    li[0]+=1
                                                if last[u] in vector2:
                                                    li[1]+=1
                                                if last[u] in vector3:
                                                    li[2]+=1
                                                if last[u] in vector4:
                                                    li[3]+=1
                                                if last[u] in vector5:
                                                    li[4]+=1
                                                if last[u] in vector6:
                                                    li[5]+=1
                                            if  not (0 in li) and li==[2,1,1,1,1,1]:
                                                print(sum(last))
                                                print((last))                                                 
                                            value.append(last)
                                            last=[]
                                  