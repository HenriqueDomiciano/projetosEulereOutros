def is_valid(string):
    var1=True
    for r in range(len(string)):
        if (string[r])>=65 and (out[r])!=32:
            var1=True and var1
        else:
            return False
    return var1

with open(r'C:\Users\Dell\Desktop\p059_cipher.txt', 'r') as f:
    lista=f.readline()
lista=lista.split(',')
biggest=[]
lista=[int(u) for u in lista]
out=[]
for r in range(97,123):
    for k in range(97,123):
        for j in range(97,123):
            list_of=[r,k,j]
            out=[]
            for i in range (len(lista)):
                var1=lista[i]^list_of[i%len(list_of)]
                if (var1>96 and var1<123) or var1==32 or var1==39:
                    out.append(var1)
            if len(out)>len(biggest):
                biggest=out
                key=[r,k,j]
#we know the key now we have to make again because it have numbers on it
out=[]
for i in range (len(lista)):
    var1=lista[i]^key[i%len(key)]
    out.append(var1)
message=[chr(u) for u in out]
message=''.join(message)
print(message)
print(sum(out))

