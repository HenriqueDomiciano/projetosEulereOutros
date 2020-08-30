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
for v1 in vector1:
    for v2 in vector2:
        if not(last_in_first(v1,v2)):
            continue
        for v3 in vector3:
            if not(last_in_first(v2,v3)):
                continue
            for v4 in vector4:
                if not(last_in_first(v3,v4)):
                    continue
                for v5 in vector5:
                    if not(last_in_first(v4,v5)):
                        continue
                    for v6 in vector6 :
                        if not(last_in_first(v5,v6)) and (not(last_in_first(v6,v1))):
                            continue
                        else:
                            val=[v1,v2,v3,v4,v5,v6]
                            print(val)
                            print(sum(val))
                            # ommproblema e a sequencia.