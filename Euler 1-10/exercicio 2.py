from math import *
dias=['sabado','domingo','segunda','terca','quarta','quinta','sexta']
ordinal=[0,31,59,90,120,151,181,212,243,273,304,334,]
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
def pascoa (ano):
    data=[]
    a=ano%19
    b=floor(ano/100)
    c= ano%100
    d=floor(b/4)
    e=b%4
    f=floor((b+8)/25)
    g=floor((1+b-f)/3)
    h=((19*a)+b+15-(d+g))%30
    i=floor(c/4)
    k=c%4
    l=(32+(2*e)+(2*i)-(h+k))%7
    m=floor(((a+(11*h)+(22*l))/451))
    p=floor(((h+l+114)-(7*m))/31)
    q=(h+l+114-(7*m))%31
    data=[q+1,p]
    return data
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
def valorcorpus(a,b,bis):
    z=ordinal[b-1]+a+60
    return z

def valorcarn(a,b,bis):
    z=ordinal[b-1]+a-47
    if bis==1:
        z=z+1
    return z;
def conversor(a,bis):
     b=[]
     if a <=31:
         b.append(1)
         b.append(a)
     elif  a>31 and a <=59:
        b.append(a-31)
        b.append(2)
     elif a > 59 and a <=90:
         if bis==1:
             b.append(a-60)
         else:
             b.append(a-59)
         b.append(3)    
     elif a > 90 and a <=120:
         b.append(a-90)
         b.append(4)
     elif a > 120 and a <=151:
         b.append(a-120)
         b.append(5)
     elif a > 151 and a <=181:
         b.append(a-151)
         b.append(6)
     elif a > 181 and a <=212:
         b.append(a-212)
         b.append(7)
        
     elif a > 212 and a <=243:
         b.append(a-243)
         b.append(8)
     return b   
ano=int(input("digite o ano"))
mes=int(input("digite o mes"))
dia=int(input("digite o dia"))
bis=bisexto(ano)
data=pascoa(ano)
a=valorcarn(data[0],data[1],bis)
b=valorcorpus(data[0],data[1],bis)
sexta=b-62
print("sexta santa ocorre no dia",conversor(sexta,bis))
print("a data do carnaval esta abaixo em dd/mm",conversor(a,bis))
print(" data do corpus christi em dd/mm",conversor(b,bis))      
print ("ambos do ano de",ano)
print("o valor ordinal de corpus christi e ",b )
print("o valor ordinal de carnaval e",a)
print("o dia da semana digitado eh",(dias[diadasemana(dia,mes,ano)]))
      

















