import math as m
def triangularnumbers(num):
      c=(num*(1+num))/2
      return c
def divisorstriangular(entrada):
      cont=0
      for div in range(1,int((entrada**0.5))+1):
            if entrada%div==0:
                  cont=cont+1
            else:
                  cont=cont
      if (entrada**0.5)%1==0:
            return cont*2-1
      else:
            return cont*2
divnum=0
a=100
while divnum<=500:
      a=a+1
      divnum=divisorstriangular(triangularnumbers(a))
print(triangularnumbers(a))
