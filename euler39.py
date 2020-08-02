import numpy as np
def find_an_value():
    vetor_quantidade=np.zeros(1001)
    for r in range(1,1000):
        for u in range(1,1000):
            c=((r**2)+(u**2))**0.5
            if (c+r+u)%1==0 and ((c+r+u)<1001):
                m=int(c+r+u)
                vetor_quantidade[m]+=1
    result=np.where(vetor_quantidade==max(vetor_quantidade))
    #result=max(vetor_quantidade)
    return result
print(find_an_value())