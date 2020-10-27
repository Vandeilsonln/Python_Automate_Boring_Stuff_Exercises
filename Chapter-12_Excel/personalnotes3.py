#! python3

import openpyxl
from os import chdir

chdir(r'Chapter-12_Excel')

workbook = openpyxl.Workbook()
sheet = workbook.active

sheet.title = 'Personal notes 3'

for row in range(1, 11):
    for col in range(1, 11):
        sheet.cell(row, col).value = row * col


workbook.save(filename='personalnotes.xlsx')