# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 18:05:08 2023

@author: Marco
"""

import pandas as pd
import numpy as np
import os
from collections import OrderedDict, Counter

# Function to remove all duplicates from string
# and order does not matter
def removeDupWithoutOrder(str):
 
    # set() --> A Set is an unordered collection
    #         data type that is iterable, mutable,
    #         and has no duplicate elements.
    # "".join() --> It joins two adjacent elements in
    #             iterable with any symbol defined in
    #             "" ( double quotes ) and returns a
    #             single string
    return "".join(set(str))
 
# Function to remove all duplicates from string
# and keep the order of characters same
def removeDupWithOrder(str):
    return "".join(OrderedDict.fromkeys(str))



def SplitString(string):
    st1 = ""
    st2 = ""
    ind=0
    if(len(string)%2==0):
        ind = int(len(string)/2)
        st1=string[:ind]
        st2=string[ind:]
        return st1, st2
    else:
        ind = int(len(string)/2)
        st1=string[:ind]
        st2=string[ind:]
        return st1, st2

def common(str1,str2):
     
    # convert both strings into counter dictionary
    dict1 = Counter(str1)
    dict2 = Counter(str2)
 
    # take intersection of these dictionaries
    commonDict = dict1 & dict2
 
    if len(commonDict) == 0:
        print (-1)
        return
 
    # get a list of common elements
    commonChars = list(commonDict.elements())
 
    # sort list in ascending order to print resultant
    # string on alphabetical order
    commonChars = sorted(commonChars)
 
    # join characters without space to produce
    # resultant string
    return ''.join(commonChars)

class Node:
    
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
      self.rep = 1
      
    # Print the node
    
    def PrintTree(self):
        print(str(self.data) + ' ' + str(self.rep))
        
        if self.left:
            self.left.PrintTree()
        
        if self.right:
            self.right.PrintTree()
                
    
    #Insert data in the last legs

    def insert(self,ext_data):
        # Check the existance of the node
        if self.data:
            # If exists, compare the external data with the actual one
            if ord(ext_data) < ord(self.data):
                # If the data is less than the actual node one, create
                # a node at its left side
                if self.left is None:
                    self.left = Node(ext_data)
                else:
                    # If the node already exists, complete it with new data
                    self.left.insert(ext_data)
            elif ord(ext_data) > ord(self.data):
                # If the data is greater or higher than the actual node one, create
                # a node at its right side
                if self.right is None:
                    self.right = Node(ext_data)
                else:
                    # If the node already exists, complete it with new data
                    self.right.insert(ext_data)
            elif ord(ext_data) == ord(self.data):
                # If the data is equal than the actual node one, create
                # a node at its right side
                self.rep += 1
        else:
            self.data = ext_data
    
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.data
    
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.data

            
    def search_multiple(self,element):
        if element == self.data:
            return self.rep
        
        if element < self.data:
            if self.left == None:
                return False
            return self.left.search_multiple(element)

        if self.right == None:
            return False
        return self.right.search_multiple(element)
        
         
                    
