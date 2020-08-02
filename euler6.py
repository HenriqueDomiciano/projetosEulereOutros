def squareofthesum(a):
      c=0
      for a in range (1,a+1):
            c=a+c
      return c**2
def sumofthesquares(a):
      c=0
      for a in range(1,a+1):
            c=a**2+c
      return c
print(squareofthesum(100)-sumofthesquares(100))            
            
    
    