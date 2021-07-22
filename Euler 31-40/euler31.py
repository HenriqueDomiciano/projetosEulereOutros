
def number_of_possibilites(test):
    val=0
    for r in range(test+1,0,-200):
        for u in range(r,0,-100):
            for m in range(u,0,-50):
                for k in range(m,0,-20):
                    for l in range(k,0,-10):
                        for n in range(l,0,-5):
                            for o in range(n,0,-2):
                                val=val+1
    return val
print(number_of_possibilites(200))