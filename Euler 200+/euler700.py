r=0
array1=[1504170715041707]

while(True):
    if r>42298632 and r<10827725431:
        r=r+283827021
    else:
        r=r+1
    value=1504170715041707*r % 4503599627370517
    
    if value<array1[-1]:
        array1.append(value)
        print(r,'-------------',value)
        #print(sum(array1),'----',array1[-1],'-----',r)
