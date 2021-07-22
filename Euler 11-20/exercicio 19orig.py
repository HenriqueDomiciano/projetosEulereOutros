from math import floor,ceil
def bisexto(ano):
    r100=bool(ano%100)
    r400=bool(ano%400)
    r4=bool(ano%4)
    r4= not r4
    r400= not r400
    if r4 and (r100 or r400):
        return 1
    else:
        return 0
def diadasemana(dia,mes,ano):
    a=floor((12-mes)/10)
    b=ano-a
    c=mes+(12*a)
    d=floor(b/100)
    e=floor(d/4)
    f=e+2-d
    g=floor(365.25*b)
    h=floor(30.6001*(c+1))
    i=f+g+h+dia+5
    r=i%7
    return r
c=-1
for ano in range (1901,2001):
      for mes in range(1,13):
            if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12: 
                  for dia in range(1,32):
                        b=diadasemana(ano,mes,dia)
                        if b==1 and dia==1:
                              c=c+1     
            elif mes==2 and bisexto(ano)==1 :
                  for dia in range(1,30):
                        b=diadasemana(ano,mes,dia)
                        if b==1 and dia==1:
                              c=c+1
            elif mes==2 and bisexto(ano)==0 :
                  for dia in range(1,29):
                        b=diadasemana(ano,mes,dia)
                        if b==1 and dia==1:
                              c=c+1
            elif mes==4 or mes==6 or mes== 9 or mes== 11:
                  for dia in range(1,31):
                        b=diadasemana(ano,mes,dia)
                        if b==1 and dia==1:
                              c=c+1   
print(c)
