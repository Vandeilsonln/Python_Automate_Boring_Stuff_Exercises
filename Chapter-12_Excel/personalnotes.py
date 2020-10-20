import openpyxl
import os

os.chdir(r'.\Chapter-12_Excel')

wb = openpyxl.load_workbook('example.xlsx')

sheet = wb.get_sheet_by_name('Planilha1')
print(sheet['A1'])

print(sheet['A1'].value)

c = sheet['B1']
print(c.value)

string = 'Row ' + str(c.row) + ', Column ' + str(c.column) + ' is ' + str(c.value)

print(string)

print(' Cell ' + str(c.coordinate) + ' is ' + str(c.value))

print(sheet['C1'].value)

print(sheet.cell(row=1, column=2))

for i in range(1, 8, 2):
    print(i, sheet.cell(row=i, column=2).value)

print(sheet.dimensions.split(':'))