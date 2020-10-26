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
def createResults(size):
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

# create headers in Excel
def createTable(size):    # 5
    for i in range(1, size+1):
        sheet.cell(1, i+1).value = i
        sheet.cell(i+1, 1).value = i

    data = createResults(size)

    for row in sheet.iter_rows(min_col=2, min_row=2, max_col=size+1, max_row=size+1):
        pass
# send it to the worksheet
createTable(5)

# save

#workbook.save(filename='multiplicationtable.xlsx')
