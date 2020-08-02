string=''
val=1
for r in range(1,1000000):
    m=str(r)
    string=string+m
value=list(string)
val=int(value[0])*int(value[9])*int(value[99])*int(value[999])*int(value[9999])*int(value[99999])*int(value[999999])
print(val)