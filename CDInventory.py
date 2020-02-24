#------------------------------------------#
# Title: CDInventory.py
# Desc: CD Inventory using dictionaries with file read and inventory delete
# functionality built-in.
# Change Log: (Who, When, What)
# DOranski, 2020-Feb-23, Created file with header.
# DOranski, 2020-Feb-24, Reduced file complexity and number of variables.
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstDic = [] # list of dictionaries to hold data
RlstDic = [] # list to hold list for deletion revert 
dicRow = {}  # list of data row
LRow = {} # for loaded data
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# -- PROCESSING -- #
# -- PRESENTATION (INPUT/OUTPUT) -- #
import os
print('The Magic CD Inventory\n')
while True:
    # Populates the user menu.
    print('[l] Load Inventory from File\n[p] Print Inventory in Memory')
    print('[a] Add a CD to Inventory in Memory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to File\n[x] Exit')
    strChoice = input('l, p, a, d, s or x: ').lower()  # convert choice to lower case at time of input
    if strChoice == 'x':
        # Exits the program.
        break
    if strChoice == 'l':
        lstDic = [] #Prevents creating a repeating list if the file is loaded continuously.
        if os.path.exists(strFileName): # Checks for existence of file.
            # Loads data from a file.
            with open(strFileName, 'r') as objFile:
                for row in objFile:
                    n = len(lstDic) + 1
                    LRow = row.strip().split(',')
                    dicRow = {'ID': n, 'Title': LRow[1], 'Artist': LRow[2]}
                    lstDic.append(dicRow)
            # Formatting for user output. 
            print()
            print('The Following Was Loaded From ' + strFileName + ':')
            print()
            print('ID, CD Title, Artist')
            for row in lstDic:
                print(*row.values(), sep = ', ')
            print()
        else:
            # Creation of file.
            with open(strFileName, 'a') as objFile:
                print('File Created')
                print()
    elif strChoice == 'a':
        # Adds data to the existing list of dictionaries.
        strID = len(lstDic) + 1
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        print()
        dicRow = {'ID': strID, 'Title': strTitle, 'Artist': strArtist}
        lstDic.append(dicRow)
    elif strChoice == 'p':
        # Displays the current data in memory.
        print()
        print('ID, CD Title, Artist')
        for row in lstDic:
            print(*row.values(), sep = ', ')
        print()
    elif strChoice == 'd':
        # Deletes entries from the current dataset.
        RlstDic = []
        print()
        print('You must save the file for the deletion to take effect!')
        delID = input('Enter the ID of the CD to delete: ')
        print()
        delID = int(delID) - 1
        if delID in range(len(lstDic)):
            for row in lstDic:
                RlstDic.append(row)
            del(lstDic[delID])
            print('ID, CD Title, Artist')
            for row in lstDic:
                print(*row.values(), sep = ', ')
            # Allows the user to revert deletion changes.
            delrev = input('Keep Changes? (y/n): ')
            print()
            if delrev == 'y':
                continue
            elif delrev == 'n':
                lstDic = RlstDic
            else:
                continue    
        else:
            print('Please select an existing value!')
            print()
    elif strChoice == 's':
        print()
        print('Saving will overwrite the current file with the inventory in memory!')
        savin = input('Are you sure? (y/n): ')
        print()
        if savin == 'y':
            # Saves the data in memory to file.
            objFile = open(strFileName, 'w')
            for row in lstDic:
                strRow = ''
                for item in row.values():
                    strRow += str(item) + ','
                strRow = strRow[:-1] + '\n'
                objFile.write(strRow)
            objFile.close()
        elif savin == 'n':
            continue
        else:
            continue
    else:
        print('Please choose either l, a, i, d, s or x!')