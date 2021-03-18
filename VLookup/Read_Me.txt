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