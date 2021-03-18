# PURPOSE
# -------------------
"""
    Consider a scenario, you are having a huge list of files wherein each File has certain
    list of requirements in them and all the information is stored into a text file "Text_File1.txt".
    Ex :
    TP_REQ_FILE_1 - 23523, 23652, 12253, 45263
    TP_REQ_FILE_2 - 85698, 12368, 12536, 87569
    TP_REQ_FILE_3 - 52369, 12583, 12586, 12539

    Data stored in "Text_File1.txt" is in the format :
    23523, 23652, 12253, 45263
    85698, 12368, 12536, 87569
    52369, 12583, 12586, 12539
    
    Now you have got list of requirement ID's which are updated, stored in another text file "Text_File2.txt"
    Ex :
    REQ23523
    REQ12368
    REQ12586

    Generate a file that maps between these two Input files and find which file needs to be updated and which requirements in that file are updated
"""

# Import python module os
import os

# Initilize variables that holds path for both the input files
Text_File1 = r'C:\Users\Raghavapurapu Eswar\Desktop\Text_File1.txt'
Text_File2 = r'C:\Users\Raghavapurapu Eswar\Desktop\Text_File2.txt'

# Open the Input files in read mode and read the lines in each of these text files
TFile1 = open(Text_File1,'r')
TFile2 = open(Text_File2,'r')
TFile_lines1 =TFile1.readlines()
TFile_lines2 = TFile2.readlines()

#Close the Input files
TFile1.close()
TFile2.close()

# Intialize a variable that holds Index
index=0

# Initialize two lists
List_Var1 = []
List_Var2 = []

# Store each line of second text file into list
for each in TFile_lines2:
    List_Var2.append(each[:-1])

# Navigate through each lines of First text file                  
for each in TFile_lines1:
    index=index+1    
    if ',' in each:        
        for word in each.split(','):
            if '\n' in word:
                List_Var1.append("REQ"+word[:-1].lstrip().strip())
            else:
                List_Var1.append("REQ"+word.lstrip().strip())
        #print (lists)
        if any(x in List_Var2 for x in List_Var1):
            print("TP_REQ_FILE_"+str(index).zfill(3))
        for each in List_Var1:            
            if each in List_Var2:
                print(each)
        #print (lists)
        List_Var1.clear()
    else:
        if "REQ"+each[:-1].lstrip().strip() in List_Var2:
            print("TP_REQ_FILE_"+str(index).zfill(3))
            print("REQ"+each[:-1].lstrip().strip())
