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

'''            
for v1 in vector1:
    for v2 in vector2:
        for v3 in vector3:
            for v4 in vector4:
                for v5 in vector5:
                    for v6 in vector6 :
                        if last_in_first(v1,v2) and last_in_first(v2,v3) and last_in_first(v3,v4) and last_in_first(v4,v5) and last_in_first(v5,v6):
                            val=[v1,v2,v3,v4,v5,v6]
                            print(val)
'''
#não encontro o erro