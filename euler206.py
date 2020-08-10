for r in range(135100000,1400000000):
    m=r**2
    e=list(str(m))
    if e[0]=='1' and e[2]=='2' and e[4]=='3' and e[6]=='4' and e[16]=='9' and e[8]=='5' and e[10]=='6' and e[12]=='7' and e[14]=='8':
        print(m,'------',r)
        break