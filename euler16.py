import time
start_time=time.time()
def  valordassomas():
      vetor=[]
      numero=2**1000
      b=str(numero)
      d=len(b)
      for a in range (1,d+1):
            val1=numero%(10**a)
            val1=val1-numero%(10**(a-1))
            val1=val1/(10**(a-1))
            vetor.append(val1)
      print((sum(vetor)))
valordassomas()
print('%s segundos'%(time.time()-start_time))