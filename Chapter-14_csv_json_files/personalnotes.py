from os import chdir
import csv


chdir(r'.\Chapter-14_csv_json_files')

outputFile = open('output.csv', 'w', newline='')

outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello', 'world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])

outputFile.close()
