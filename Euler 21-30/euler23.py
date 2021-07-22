import math
all_numbers = list(range(1,28125))

def is_abundant(x):
    divisors= []
    for i in range(2,math.ceil(x**0.5)):
        if x%i==0:
            divisors.append(x//i)
            divisors.append(i)
    if int(x**0.5)**2==x:
        divisors.append(int(x**0.5))
    return sum(divisors)>x
all_abundant_numbers = []
for i in all_numbers:
    if is_abundant(i):
        all_abundant_numbers.append(i)
sum_of_abu = []
print(len(all_abundant_numbers))
for i in range(len(all_abundant_numbers)):
    for j in range(i,len(all_abundant_numbers)):
        sum_of_abu.append(all_abundant_numbers[i]+all_abundant_numbers[j])
for i in set(sum_of_abu):
    try:
        all_numbers.pop(all_numbers.index(i))
    except:
        break
print(sum(all_numbers))



