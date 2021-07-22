n=100

def factorial(x):
    count=1
    for m in range(x,1,-1):
        count*=m
    return count

def binomium(x,y):
    return (factorial(x)/(factorial(x-y)*factorial(y)))

count=0

for x in range(1,n+1):
    for y in range(0,(x//2)+1):

        if binomium(x,y)%7==0 and y==x//2 and x%2==0 :

            print(binomium(x,y))
            count+=1

        elif binomium(x,y)%7==0 :

            print(binomium(x,y),'2')
            count+=2
print(count)