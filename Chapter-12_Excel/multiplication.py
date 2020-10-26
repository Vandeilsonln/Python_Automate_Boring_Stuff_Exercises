#! python3
# multiplication.py - Creates a excel spreadsheet with a 
# multiplication table inside


import openpyxl
from os import chdir

# set up directory
chdir(r'Chapter-12_Excel')

# create a workbook and a sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# create a function to build the table
def createTable(size):
    # size: integer
    # return: list
    myTable = []

    for colnum in range(1, size+1):
        # myTable will have a list inside for each row
        dataTable = []
        for rownum in range(1, size+1):
            result = colnum * rownum
            dataTable.append(result)
        myTable.append(dataTable)

    return myTable
# create headers

# send it to the worksheet

# save

print(createTable(5))