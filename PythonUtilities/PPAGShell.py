# -*- coding: utf-8 -*-

#purpose of the program: select dll from folder path and copy dlls into a new path

import os, shutil

dll_path = input("Enter the dll folder path:") #Enter by command line the path of the vstore
dll_path = os.path.realpath(dll_path)          #Translate Windows path to Python path convention


file_names = os.listdir(dll_path)          #Put in the list all the files inside the
                                           #folder already inserted
dll = []      #destination folder

for i in file_names:
    if(str(i).endswith('.dll')):
        #print(dll_path + '\\' + str(i))        
        dll.append(dll_path + '\\' + str(i))      #insert all dll files with previous path

vstore_path= input("\nEnter the vstore path:")     #destination of the dll copies
vstore_path = os.path.realpath(vstore_path) 

for i in dll:
    shutil.copy(i, vstore_path)        #copy operation from dll list

