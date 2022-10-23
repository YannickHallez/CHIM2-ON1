from pylab import *
import random
    

def genereC(num):
    C=[]
    for i in range(num):
        v=random.gauss(0,0.2)+4
        C.append(round(v,2))
    return C

def decC():
    C=[]
    num=2000
    for i in range(num):
        v=random.gauss(0,0.05)+4*exp(-float(i)/500.0)
        C.append(round(v,3))
    return C



    