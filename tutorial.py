from numpy import *
from scipy import *
from matplotlib import *
import random

def MatrixCreate(inta,intb):
    arr = zeros([inta,intb])
    arr2 = list(arr[0])
    return arr2

def MatrixRandomize(v):
    x = 0
    while x<(size(v)):
        #print x
        v[x] = random.random()
        x += 1
        
    return v

def Fitness(v):
    x = 0
    j = 0
    while x<(size(v)):
        yu = v[x]
        j = j + yu
        x += 1

    i = j/(size(v))

    return i

def MatrixPerturb(v,per):
    p = list(v)
    xx = random.random()
    yy = size(p)
    xy = 0

    while xy<yy:
        if(xx<per):
            p[xy] = random.random()
            
        xx = random.random()
        xy += 1
        
    return p

def RTDT(dd):
    parent = MatrixCreate(1,50)
    fits = MatrixCreate(1,dd)
    
    parent = MatrixRandomize(parent)
    parentFitness = Fitness(parent)
    
    for currentGeneration in range(0,dd):
        print currentGeneration, parentFitness
        child = MatrixPerturb(parent,0.05)
        childFitness = Fitness(child)
        if(childFitness>parentFitness):
            parent = child
            parentFitness = childFitness
        fits[currentGeneration] = parentFitness

    return fits


    
    
    
