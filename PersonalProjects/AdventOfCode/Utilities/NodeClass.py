# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 18:05:08 2023

@author: Marco
"""

class Node:
    
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
      self.rep = 0
      
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
            if ext_data < self.data:
                # If the data is less than the actual node one, create
                # a node at its left side
                if self.left is None:
                    self.left = Node(ext_data)
                else:
                    # If the node already exists, complete it with new data
                    self.left.insert(ext_data)
            elif ext_data > self.data:
                # If the data is greater or higher than the actual node one, create
                # a node at its right side
                if self.right is None:
                    self.right = Node(ext_data)
                else:
                    # If the node already exists, complete it with new data
                    self.right.insert(ext_data)
            elif ext_data == self.data:
                # If the data is equal than the actual node one, create
                # a node at its right side
                self.rep += 1
        else:
            self.data = ext_data


TopNode = Node(3)
TopNode.insert(4)
TopNode.insert(2)
TopNode.insert(2)
TopNode.insert(2)

TopNode.PrintTree()

                
                    
