import openpyxl
import os

os.chdir(r'.\Chapter-12_Excel')

myWorkBook = openpyxl.Workbook()
mySheet = myWorkBook.active

mySheet['A1'] = 'Hello'
mySheet['A2'] = 'world!'

myWorkBook.save(filename='hello_world.xlsx')