import openpyxl
import os

os.chdir(r'.\Chapter-12_Excel')

myWorkbook = openpyxl.load_workbook('example.xlsx')

print(myWorkbook.sheetnames)

mySheet = myWorkbook.active
print(mySheet)
print(mySheet.title)
