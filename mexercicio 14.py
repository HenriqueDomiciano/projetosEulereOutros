def determinarsequencia(a):
      c=0
      while a!=1:
            if a%2==0:
                  a=a/2
                  c=c+1
            else:
                  a=3*a+1
                  c=c+1
      return c
def funcaodecontagem():
      vetornum=[]
      valfix=0
      for b in range (21,1000001):
                  if determinarsequencia(b)>=valfix:
                        valor=b
                        valfix=determinarsequencia(b)
                  else:
                        valfix=valfix
      print(valor)
funcaodecontagem()                       
                        
                  
            
