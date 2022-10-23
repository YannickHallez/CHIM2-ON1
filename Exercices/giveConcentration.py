import random
    

def genereC(num):
    C=[]
    for i in range(num):
        v=random.gauss(0,0.2)+4
        C.append(round(v,2))
    return C



    