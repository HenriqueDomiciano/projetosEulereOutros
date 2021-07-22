import time
start_time=time.time()
def split(x): 
    x=str(x)
    x=x.replace('0b','')
    val=list(x)
    lista_1=[]
    for values in val : 
        lista_1.append(int(values))
    return(lista_1)
def test_palindrome(list_1):
    value_2=list_1[::-1]
    if value_2==list_1:
        return True
    else: 
        return False
val=0

for r in range(1,1000000):
    if test_palindrome(split(r)) and (test_palindrome(split(bin(r)))):
        val=val+r
print(val)
print('--------%s segundos'%(start_time-time.time()))