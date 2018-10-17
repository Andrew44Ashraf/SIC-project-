import numpy as np 
import random
import uuid
from declerations import *

f = open('SIC_input.asm','w')

num_inst = random.randint(5,200)
num_labels = (int)(num_inst/random.randint(2,num_inst-1))
num_variables = (int)(num_inst/random.randint(2,num_inst-1))
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
prog_name=""
while(True):
    prog_name=''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(4))
    if(checktaken(prog_name)==False):
        break
code.append("COPY START 1000")


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
random_points=list(range(2,num_inst+1))
random.shuffle(random_points)
random_points=random_points[:num_labels]


i=0
for point in random_points:
    code[point]=labels[i]+" "+code[point]
    i=i+1



# rserve variables
for i in range(num_variables):
    s=""
    j=random.randint(0,3)
    s+=variables[i]+" "+RES_INST[j]+" "+str(random.randint(1,2))
    code.append(s)
    #print(s)

code[1]=prog_name+" "+code[1]
code.append("END "+prog_name)
#Print out code
print("Generated code of size: " + str(len(code)))
for i in code:
    f.write(i+'\n')

# To do: -strin
