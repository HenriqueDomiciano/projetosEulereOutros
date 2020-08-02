rotor1=['c','d','z','r','m','g','h','x','a','w','q','v','u','f','s','b','p','l','t','o','e','i','y','n','k','j']
rotor2=['v','e','w','o','a','s','x','d','h','r','c','y','q','j','n','p','t','k','b','l','m','f','u','z','g','i']
rotor3=['i','p','r','n','f','m','w','o','z','j','q','c','x','g','t','d','b','k','e','l','y','v','a','h','s','u']
rotor4=['d','q','n','t','s','x','z','r','o','j','b','a','k','c','g','e','y','p','u','i','h','f','l','m','v','w']
rotor5=['b','k','q','s','l','p','m','d','c','a','n','y','h','g','i','r','z','v','j','f','t','u','x','e','o','w']
rebound=['o','k','y','x','v','g','f','s','t','q','b','w','n','m','a','u','j','z','h','i','p','e','l','d','c','r']
letra_digitada=[]
con=[]
for a in range (0,12):
    valor=input("digite as 6 conexoes")
    con.append(valor)            
factbet=[]
alfabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
factbet=alfabet
def transfer(alfabeto,b):
    par1= b[0:2]
    par2=b[2:4]
    par3=b[4:6]
    par4=b[6:8]
    par5=b[8:10]
    par6=b[10:12]
    a=alfabeto.index(par1[0])
    b=alfabeto.index(par2[0])
    c=alfabeto.index(par3[0])
    d=alfabeto.index(par4[0])
    e=alfabeto.index(par5[0])
    f=alfabeto.index(par6[0])
    a1=alfabeto.index(par1[1])
    b1=alfabeto.index(par2[1])
    c1=alfabeto.index(par3[1])
    d1=alfabeto.index(par4[1])
    e1=alfabeto.index(par5[1])
    f1=alfabeto.index(par6[1])
    val1=alfabeto[a]
    val2=alfabeto[b]
    val3=alfabeto[c]
    val4=alfabeto[d]
    val5=alfabeto[e]
    val6=alfabeto[f]
    print(val1)
    print(val2)
    alfabeto[a]=alfabeto[a1]
    alfabeto[b]=alfabeto[b1]
    alfabeto[c]=alfabeto[c1]
    alfabeto[d]=alfabeto[d1]
    alfabeto[e]=alfabeto[e1]
    alfabeto[f]=alfabeto[f1]
    alfabeto[a1]=val1
    alfabeto[b1]=val2
    alfabeto[c1]=val3
    alfabeto[d1]=val4
    alfabeto[e1]=val5
    alfabeto[f1]=val6
    print(alfabeto)
    return alfabeto
def   distrirot(rot,rot1,rot2,rot3,rot4,rot5):
    if rot==1:
        rot=rot1
    elif rot==2:
        rot=rot2
    elif rot==3:
        rot=rot3
    elif rot==4:
        rot=rot4
    else:
        rot=rot5
    return rot 
def encontrarletra(a,rot,alfabet):
            val=alfabet.index(a)
            return rot[val]
def inicializaçao(rotor,a,alphabet):
    n=alphabet.index(a)
    m=rotor[n:-1]
    u=rotor[0:n]
    rotor1=[]
    rotor1.extend(m)
    rotor1.extend(u)
    return rotor1
    
        
letra_digitada.append(input("digite a letra 1"))
letra_digitada.append(input("digite a letra 2"))
letra_digitada.append(input("digite a letra 3"))
letra_digitada.append(input("digite a letra 4"))
rt1=int(input("digite o primeiro rotor"))
rt2=int(input("digite o segundo rotor"))
rt3=int(input("digite o terceiro rotor"))
rimrot=distrirot(rt1,rotor1,rotor2,rotor3,rotor4,rotor5)
egrot=distrirot(rt2,rotor1,rotor2,rotor3,rotor4,rotor5)
errot=distrirot(rt3,rotor1,rotor2,rotor3,rotor4,rotor5)
valr=transfer(factbet,con)
primrot=inicializaçao(rimrot,input("valor primeira letra"),factbet)
segrot=inicializaçao(egrot,input("valor da segunda letra"),factbet)
terrot=inicializaçao(errot,input("valor da segunda letra"),factbet)
a0=encontrarletra(letra_digitada[0],valr,alfabet)
print(a0)
a=encontrarletra(a0,primrot,alfabet)
print(a)
b=encontrarletra(a,segrot,alfabet)
print(b)
c=encontrarletra(b,terrot,alfabet)
print(c)
d=encontrarletra(c,rebound,alfabet)
print(d)



