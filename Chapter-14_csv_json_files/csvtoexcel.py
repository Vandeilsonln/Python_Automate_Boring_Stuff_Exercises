#! python3
# csvtoexcel.py - Copy specific data from a CSV file to an Excel Spreadsheet

import csv
import openpyxl
from os import chdir

chdir(r'Chapter-14_csv_json_files')
#Open the csv file
with open('output.csv', 'r') as csvFile:
    readerCsvFile = csv.reader(csvFile)
    #Loop through every line of the csv file
    for row in readerCsvFile:
        

#TODO: Create the excel spreadsheet

#TODO: Write the csv object to the excel one.