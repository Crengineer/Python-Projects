# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 20:00:26 2023

@author: Marco
"""

import numpy as np
import pandas as pd
import os

# data

ref = 0
max_cal = 0
space_c = 0

# file

file = open("C:/Users/New/Desktop/AdventOfCode/Day1/Day1.txt",'r')

with open("C:/Users/New/Desktop/AdventOfCode/Day1/Day1.txt") as f:
    contents = f.readlines()

col = pd.DataFrame(data=contents, columns=["Value"])

for i in col["Value"]:
    if(i=='\n'):
        space_c+=1
        ref=0;
    elif (i!='\n'):
        ref+=int(i)
        print(ref)
        print("Maximum value: " + str(max_cal))
        if(ref>=max_cal):
            max_cal = ref
            

print(space_c)
print(max_cal)