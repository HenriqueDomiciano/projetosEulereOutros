def split(x): 
    x=str(x)
    val=list(x)
    lista_1=[]
    for values in val : 
        lista_1.append(int(values))
    return(lista_1)
def test_if_is_number(list1,n):
    new_array=[]
    for values in list1:
        new_array.append(values**5)
    if sum(new_array)==n:
        return True
c=0
for r in range(0,8000000):
    if test_if_is_number(split(r),r):
        c=c+r
print(c-1)