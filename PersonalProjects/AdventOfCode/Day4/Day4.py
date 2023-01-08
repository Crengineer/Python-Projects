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

file = open("C:/Users/New/Desktop/AdventOfCode/Day4/Day4.txt",'r')

with open("C:/Users/New/Desktop/AdventOfCode/Day4/Day4.txt") as f:
    contents = f.readlines()
    
    
# DATA

counter = 0

def Day4FirstChallenge():
    
    for line in contents:
        line = line.translate({ord(c): None for c in string.whitespace}) #remove space, tabs, newline
        line = line.replace('-', ' ') # substitute minus with space
        line = line.replace(',', ' ') # subsitute comma with space
        line = line.split()           #create a list from the words separated by space
        if((int(line[0]) <= int(line[2]) and int(line[3]) <= int(line[1])) or (int(line[2]) <= int(line[0]) and int(line[1]) <= int(line[3]))):
            counter += 1
            
for line in contents:
        line = line.translate({ord(c): None for c in string.whitespace}) #remove space, tabs, newline
        line = line.replace('-', ' ') # substitute minus with space
        line = line.replace(',', ' ') # subsitute comma with space
        line = line.split()           #create a list from the words separated by space
        if(not((int(line[0]) < int(line[3]) and int(line[1]) < int(line[2])) or (int(line[3]) < int(line[0]) and int(line[2]) < int(line[1])))):
            counter += 1
    