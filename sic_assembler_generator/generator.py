import numpy as np 
import random
import uuid
from declerations import *

def gen_code(debug_flag=False, save_to_file=True,ub=0):
   # print(ub)
    num_inst = random.randint(5,5+ub)
    num_labels= min(4,(int)(num_inst/5)) #(int)(num_inst/random.randint(2,min(5,num_inst-1)))
    num_variables=min(4,(int)(num_inst/5)) #(int)(num_inst/random.randint(2,num_inst-1))
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
            s="VAR"+str(i)
            break
            if(checktaken(s)==False):
                break
        variables.append(s)
    for i in range(0,num_labels):
        while(True):
            s=''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(4))
            s="LAB"+str(i)
            break
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
    code.append(prog_name + " START 1000")


    #instruction generation 
    for i in range(num_inst):
        s=""
        j=random.randint(0,len(INST)-1)
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



    def gen_x():
        prog_name=''.join(random.choice('ABCDEF0123456789') for i in range(random.randint(1,6)));
        return "'"+prog_name+"'";

    # rserve variables
    for i in range(num_variables):
        s=""
        j=random.randint(0,3)
        if(j<2):
            s+=variables[i]+" "+RES_INST[j]+" "+str(random.randint(1,4))
        elif (j==2):
            s+=variables[i]+" "+RES_INST[j]+" X"+gen_x()
        else:
            p=''.join(random.choice('0123456789') for i in range(random.randint(1,6)));
            s+=variables[i]+" "+RES_INST[j]+" "+str(p)
        
        code.append(s)
        #print(s)

    #code[1]=prog_name+" "+code[1]
    code.append("END "+prog_name)
    #Print out code
    if(debug_flag==True):
        print("Generated code of size: " + str(len(code)))
    if(save_to_file==True):
        f=open("intermediate.txt","w")
        for line in code:
            f.write(line)
            f.write("\n")
        
    return code
    # To do: -strin
