# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 21:39:35 2023

@author: Marco
"""
import numpy as np
import pandas as pd
import os

# data

col1 = []
col2 = []
score = 0

# file

file = open("C:/Users/New/Desktop/AdventOfCode/Day2/Day2.txt",'r')

with open("C:/Users/New/Desktop/AdventOfCode/Day2/Day2.txt") as f:
    contents = f.readlines()

for i in contents:
    col1.append(i[0])
    col2.append(i[2])

# Rock = 1 P
# Paper = 2 P
#Scissors = 3 P

#Lose = 0 P
#Draw = 3 P
#Win  = 6 P

# Matrix points due to winning

Mat_win = np.array([[3,6,0],
       [0,3,6],
       [6,0,3]])

Mat_sign = np.array([[1,2,3],
       [1,2,3],
       [1,2,3]])

Mat_win = Mat_win+Mat_sign

Mat = pd.DataFrame(data=Mat_win,index=['A','B','C'],columns=['X','Y','Z'])

for i in range(len(col1)):
    score+=Mat.loc[col1[i],col2[i]]

print(score)

#Part 2

Mat_win = np.array([[0,3,6],
       [0,3,6],
       [0,3,6]])

Mat_sign = np.array([[3,1,2],
       [1,2,3],
       [2,3,1]])

Mat_win = Mat_win+Mat_sign
Mat = pd.DataFrame(data=Mat_win,index=['A','B','C'],columns=['X','Y','Z'])
score2 = 0

for i in range(len(col1)):
    score2+=Mat.loc[col1[i],col2[i]]

print(score2)