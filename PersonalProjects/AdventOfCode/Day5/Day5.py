# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 20:01:11 2023

@author: Marco
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 18:00:42 2023

@author: Marco
"""

import numpy as np
import pandas as pd
import os
import string
from collections import OrderedDict

file = open("C:/Users/New/Desktop/AdventOfCode/Day5/Day5.txt",'r')

with open("C:/Users/New/Desktop/AdventOfCode/Day5/Day5.txt") as f:
    contents = f.readlines()
    

#DATA

upp_case = list(string.ascii_uppercase)  # used to check the presence of cranes

cranes = contents[0:9]   # Cranes in piles representation
instr = contents[10:]    # Cranes movement instructions
cols = cranes[-1].split()  # Set of piles
total = []
pile = []  #reference list for every column

piles_lists = []

for i in range(len(cols)):
    piles_lists.append(pile)

counter = 0
for i in range(1, len(cranes[0]), 4):    
    for j in cranes[:-1]:
        #print(j[i])
        pile.append('['+j[i]+']')
    piles_lists[counter] = pile
    pile = []
    counter+=1

line = []
for i in range(len(piles_lists)):
    for j in range(len(piles_lists[i])):
        if(piles_lists[i][j][1] in upp_case):
            line.append(piles_lists[i][j])
    piles_lists[i] = line
    line = []

for x in piles_lists:
    x = x.reverse()

instr2= []
line = []
for x in instr:
    line = x.split()
    instr2.append(line)

def Day5ChallengePartOne():
    
    # pile_lists, instr2
    quantity = 0
    start_ind = 0
    end_ind = 0
    temp = ''
    for x in instr2:
        print(x)
        quantity = int(x[1])
        start_ind = int(x[3])-1
        end_ind = int(x[5])-1
        print(quantity)
        print(start_ind)
        print(end_ind)
        for y in range(0,quantity):
            print(y)
            print(piles_lists[start_ind])
            temp = piles_lists[start_ind][-1]
            print(temp)
            piles_lists[start_ind].pop()
            print(piles_lists[start_ind])
            piles_lists[end_ind].append(temp)
    
    final = []
    for x in piles_lists:
        final.append(x[-1])
            
# pile_lists, instr2
quantity = 0
start_ind = 0
end_ind = 0
temp = ''
line = []
for x in instr2:
    print(x)
    quantity = int(x[1])
    start_ind = int(x[3])-1
    end_ind = int(x[5])-1
    print(quantity)
    print(start_ind)
    print(end_ind)
    for y in range(0,quantity):
        print(y)
        print(piles_lists[start_ind])
        temp = piles_lists[start_ind][-1]
        print(temp)
        piles_lists[start_ind].pop()
        print(piles_lists[start_ind])
        #piles_lists[end_ind].append(temp)
        line.append(temp)
    print(line)
    line.reverse()
    for z in line:
        piles_lists[end_ind].append(z)
    line = []
        
final = []
for x in piles_lists:
    final.append(x[-1])