import numpy as np 
import random
import uuid
from declerations import *


num_inst = random.randint(5,21)
num_labels = (int)(num_inst/random.randint(2,6))
num_variables = (int)(num_inst/random.randint(2,6))
variables=[]
labels=[]
name_set=set()

def checktaken(s):
    if(s in name_set):
        return True
    else:
        name_set.add(s)
        return False




#genrate random labels and ids
for i in range(0,num_variables):
    while(True):
        s=''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(4))
        if(checktaken(s)==False):
            break
    variables.append(s)
for i in range(0,num_labels):
    while(True):
        s=''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(4))
        if(checktaken(s)==False):
            break
    labels.append(s)
code=[]

#Start Program
while(True):
    s=''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(4))
    if(checktaken(s)==False):
        break
s+= " START 1000"
code.append(s)


#instruction generation 
for i in range(num_inst):
    s=""
    j=random.randint(0,13-1)
    s=s+str(INST[j])
    if(OP[INST[j]]=='v'):
        j=random.randint(0,num_variables-1)
        s+=" "+variables[j]
    else:
        j=random.randint(0,num_labels-1)
        s+=" "+labels[j]

    code.append(s)
    #print(s)

#assign labels
random_points=list(range(1,num_inst+1))
random.shuffle(random_points)
random_points=random_points[:num_labels]
print(random_points)

i=0
for point in random_points:
    code[point]=labels[i]+" "+code[point]
    i=i+1



# rserve variables
for i in range(num_variables):
    s=""
    j=random.randint(0,3)
    s+=RES_INST[j]+" "+variables[i]+" "+str(random.randint(1,4))
    code.append(s)
    #print(s)

#Print out code
for i in code:
    print (i)
# To do: -strin
