from os import chdir
import csv


chdir(r'.\Chapter-14_csv_json_files')

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

for i in exampleData:
    print(i)
print('-' * 40)

print(exampleData[0][1])
print(exampleData[2][0])
print(exampleData[6][2])

