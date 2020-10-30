from os import chdir
import csv
import os

for i in os.listdir:
    print(i)

chdir(r'.\Chapter-14_csv_json_files')

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

print(exampleData)