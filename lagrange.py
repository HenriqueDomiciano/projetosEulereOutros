import numpy as np
def lagrange(x,y,X):
    
    n=(len(x))
    i=0
    j=0
    Yr=0
    
    while i<n:
        Y=1
        while j<n:
            if j!=i:
                Y=Y*((X-x[j])/(x[i]-x[j]))
                j=j+1
            else:
               j=j+1
        j=0
        Y=y[i]*Y
        Yr=Y+Yr
        i=i+1
        
    print(Yr)

x=np.array([1950,1960,1970],float)
y=np.array([151.326,179.323,203.302],float)
X=1963

lagrange(x,y,X)
