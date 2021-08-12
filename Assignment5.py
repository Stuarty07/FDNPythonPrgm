# =============================================================================
# #------------------------------------#
# # Title: <Enter Title Here.py>
# =============================================================================
# Desc: <Code Description>
# change log: (Who, When, What)
# <AYinka, Sun Aug  8 14:34:22 2021 Createdfile> 
#-----------------------------------#
# Declare variabls

strChoice = '' # User input
lstDic = []  # list of dictionary to hold data
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
#--PROCESSING--#
# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()
    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        lstDic= []
        objF = open(strFileName, 'r')
        for row in objF:
            rowA = row.strip().split('|')
            dicRow = {'id': int(rowA[0]), 'name': rowA[1], 'email': rowA[2]}
            lstDic.append(dicRow)
            print(lstDic)
        objF.close()
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        ID = int(input('Enter an ID: '))
        Title = input('Enter the CD\'s Title: ')
        Artist = input('Enter the Artist\'s Name: ')
        tempDict = {'ID': ID, 'Title': Title, 'Artist': Artist}
        lstDic.append(tempDict)
        #--PRESENTATION (Input/Output)--#
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print(lstDic)
        print("\n")
    elif strChoice == 'd':
        id1 = int(input('Enter the ID of the inventory to delete:' ))
        for row in lstDic:
            if row['ID'] == id1:
                lstDic.pop(lstDic.index(row))
        print(lstDic)
        pass
    elif strChoice == 's':
        inRow = ''
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objF = open(strFileName, 'w')
        for item in lstDic:
            for row in item.values():
                inRow += str(row) + '|'
            objF.write(inRow + "\n")
        objF.close()
    else:
        print('Please choose either l, a, i, d, s or x!')