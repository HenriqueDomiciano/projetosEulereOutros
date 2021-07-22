def generate():
   d=1
   while d!=0 :
    for a in range (1,30):
       for b in range (1,30):
           l1=(a**2)-(b**2)
           l2=2*a*b
           l3=(a**2)+(b**2)
           if l1+l2+l3==1000 and l1>0 and l2>0 and l3>0:
               return l1*l2*l3
           else:
               a=a
print(generate())               
