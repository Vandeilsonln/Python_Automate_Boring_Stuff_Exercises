import openpyxl
import os

os.chdir(r'.\Chapter-12_Excel')

myWorkbook = openpyxl.load_workbook('example.xlsx')

mySheet = myWorkbook.active

print(mySheet['A1:C2'])

print('-'*40)

for row in mySheet.iter_rows(min_row=1, max_row=4, min_col=1, max_col=5):
    print(row)

print('-'*40)

for column in mySheet.iter_cols(min_row=1, max_row=4, min_col=1, max_col=5):
    print(column)

print('-'*40)

