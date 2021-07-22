def factorial(n):
      fat=1
      for a in range (n,1,-1):
            fat=a*fat
      return str(fat)
def somador(a):
      vetor=[]
      c=len (a)
      a=int(a)
      for b in range(1,c+1):
            val1=a%(10**b)
            val1=val1-a%(10**(b-1))
            val1=val1/(10**(b-1))
            vetor.append(val1)
      print(vetor)      
      return sum(vetor)
#print(somador(factorial(100)))
print(factorial(9))