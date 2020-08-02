import numpy as np
def Newton(x,y,X):
    n=len(x)
    m=n-1
    i=0
    delta=[0]*n
    coef=[0]*n
    
    while i<(n-1):
        delta[i]=((y[i+1])-(y[i]))/((x[i+1])-(x[i]))
        i=i+1
    coef[0]=delta[0]
    
    deltanovo=[0]*n
    
    q=n-2
    p=2
    t=0
    i=0
    r=1
    
    while t<=m:
        i=0
        while i<(q):
            deltanovo[i]=((delta[i+1])-(delta[i]))/((x[p+i])-(x[i]))
            i=i+1
            coef[r]=deltanovo[0]
        r=r+1   
        delta=[0]*q
        j=0
        while j<q:
            delta[j]=deltanovo[j]
            j=j+1
        deltanovo=[0]*n
        t=t+1
        q=q-1
        p=p+1
    
    i=1
    j=0
    Yr=0
    o=m
    
    while i<=m:
        Y=1
        while j<(o):
            Y=Y*(X-x[j])
            j=j+1
        o=o-1
        Yr=((coef[o]*Y))+Yr
        i=i+1
        j=0
        
    Yr=Yr+y[0]
    print (Yr)
  
x=np.array([1950,1960,1970,1980],float)
y=np.array([151.326,179.323,203.302,226.542],float)
X=1963
Newton(x,y,X)
