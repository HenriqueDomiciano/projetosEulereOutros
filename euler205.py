def dice1():
    vect=[]
    for q in range(1,5):
        for q1 in range(1,5):
            for q2 in range(1,5):
                for q3 in range(1,5):
                    for q4 in range(1,5):
                        for q5 in range(1,5):
                            for q6 in range(1,5):
                                for q7 in range(1,5):
                                    for q8 in range(1,5):
                                        vect.append(sum([q,q1,q2,q3,q4,q5,q6,q7,q8]))
    return vect
def dice2():
    vect=[]
    for q in range(1,7):
        for q1 in range(1,7):
            for q2 in range(1,7):
                for q3 in range(1,7):
                    for q4 in range(1,7):
                        for q5 in range(1,7):
                            vect.append(sum([q,q1,q2,q3,q4,q5]))
    return vect                        
peter=[]
colin=[]
peter=dice1()
colin=dice2()
val=0
for r in peter:
    for i in colin:
        if peter>colin:
            val+=1
prob=val/12230590464
print(prob)
