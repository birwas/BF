from asyncore import read
import sys

file = open('input.txt','r')
program = file.read()
file.close()
pC = 0 #Program counter
data = [0] # Array for the bf program to input/output data.
dPointer = 0 # Data pointer

#Look ahead of time for brackets.
# Use stack method for matching brackets. Use their location in the program for a lookup table. 
bracketCheck = program.index('[')
brackets = {}
if(bracketCheck!=-1):
    counter= bracketCheck
    matching = []
    while(counter<len(program)):
        command = program[counter]
        if(command=="["):
            matching.append(counter)
        elif(command=="]"):
            if not len(matching):
                print("missing bracket,unmatched closing bracket at pos " + str(counter))
                quit()
            matchedLeft = matching.pop()
            brackets[matchedLeft]= counter
            brackets[counter] = matchedLeft
        counter+=1
    if len(matching):
        print("missing closed bracket from pos " + str(matching[0]))
        quit()
    

loopCycles=0
while(pC<len(program)):
    instr = program[pC]
    if(instr==">"):
        dPointer+=1
        if(dPointer==len(data)):
            data.append(0)
    elif(instr=="<"):
        dPointer-=1
    elif(instr=="+"):
        data[dPointer]+=1
        if(data[dPointer]>255):
            data[dPointer]=0
        
    elif(instr=="-"):
        data[dPointer]-=1
        if(data[dPointer]<0):
            data[dPointer]=255
        
    
    elif(instr=="."):
        print(chr(data[dPointer]), end= "")
        
    
    elif(instr==","):
        userText = input("Type something ")[0]
        data[dPointer]= ord(userText)
    
    elif(instr=="["):
        if(data[dPointer]==0):
            pc=brackets[pC]
            continue

    elif(instr=="]"):
        if(data[dPointer]!=0):
            pC=brackets[pC]
            loopCycles+=1
            continue

    pC+=1

    
    

