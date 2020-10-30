from os import chdir
import csv


chdir(r'.\Chapter-14_csv_json_files')

outputFile = open('example.csv', 'w', newline='')
csvWriter = csv.writer(outputFile, delimiter='\t', lineterminator='\n\n')

csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam'])
outputFile.close()

