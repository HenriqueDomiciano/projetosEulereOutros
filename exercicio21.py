def divisors(a):
      divisores=[]
      for b in range(1,int(a**0.5)+1):
            if a**0.5%1==0:
                  divisores.append(a**0.5)
            if a%b==0:
                  divisores.append(b)
                  divisores.append(a/b)
            else:
                  divisores=divisores
      return(sum(divisores))
def contador(a):
      vetor=[]
      #for b in range(1,10001):
      vetor.append(divisors(a))
      print(vetor)
contador(10001)

