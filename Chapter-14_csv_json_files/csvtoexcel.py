#! python3
# csvtoexcel.py - Copy specific data from a CSV file to an Excel Spreadsheet

import csv
import openpyxl
from os import chdir

chdir(r'Chapter-14_csv_json_files')

# Set up the excel spreadsheet
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = 'Exercise'

# Open the csv file
with open('output.csv', 'r') as csvFile:
    readerCsvFile = csv.reader(csvFile)
    print('Reading ' + csvFile.name)
    # Loop through every line of the csv file
    for row in readerCsvFile:
        # Write the csv object to the excel one.
        sheet.append(row)
workbook.save('csvtoexcel_ex.xlsx')
print('Finished\nWorkbook saved!')