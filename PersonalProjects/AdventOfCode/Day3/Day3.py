# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 15:20:23 2023

@author: Marco
"""

# Character range function
def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))


import numpy as np
import pandas as pd
import os
import string
from NodeClass import *
from collections import OrderedDict

file = open("C:/Users/New/Desktop/AdventOfCode/Day3/Day3.txt",'r')

with open("C:/Users/New/Desktop/AdventOfCode/Day3/Day3.txt") as f:
    contents = f.readlines()

# LISTS

alph = []
values = []
list1 = []
list2 = []
counter = 0
str1 = ""
str2 = ""
str3 = ""
ref1 = ""
ref2 = ""
ind = 1

alph=list(string.ascii_lowercase+string.ascii_uppercase)

for i in range(len(alph)):
    values.append(ind)
    ind+=1

def challengePartOneDay3():

    for line in contents:
        str1, str2 = SplitString(line) #Split the string in two equal strings
        str1 = str1.translate({ord(c): None for c in string.whitespace}) #remove space, tabs, newline
        str2 = str2.translate({ord(c): None for c in string.whitespace}) #same as above
        str1 = ''.join(sorted(str1)) #sort the string in alphabetical order
        str2 = ''.join(sorted(str2)) #same as above
        str1 = removeDupWithOrder(str1) #remove the repeated letters and put them in alphabetical order
        str2 = removeDupWithOrder(str2) #same as above
        ref = common(str1,str2)
        counter += values[alph.index(ref)]


def challengePartTwoDay3():
    
    for i in range(0, len(contents), 3):
        str1 = contents[i]
        str2 = contents[i+1]
        str3 = contents[i+2]
        # print(str1)
        # print(str2)
        # print(str3)
        str1 = str1.translate({ord(c): None for c in string.whitespace}) #remove space, tabs, newline
        str2 = str2.translate({ord(c): None for c in string.whitespace}) #same as above
        str3 = str3.translate({ord(c): None for c in string.whitespace}) #same as above
        # print("translate")
        # print(str1)
        # print(str2)
        # print(str3)
        str1 = ''.join(sorted(str1)) #sort the string in alphabetical order
        str2 = ''.join(sorted(str2)) #same as above
        str3 = ''.join(sorted(str3)) #same as above
        # print("translate")
        # print(str1)
        # print(str2)
        # print(str3)
        str1 = removeDupWithOrder(str1) #remove the repeated letters and put them in alphabetical order
        str2 = removeDupWithOrder(str2) #same as above
        str3 = removeDupWithOrder(str3) #same as above
        # print("translate")
        # print(str1)
        # print(str2)
        # print(str3)
        ref1 = common(str1,str2)
        # print("Common 1 and 2")
        # print(ref1)
        ref2 = common(ref1,str3)
        counter += values[alph.index(ref2)]
        # print("Common 1 and 2 and 3")
        # print(ref2)
        print(counter)