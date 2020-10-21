from openpyxl import load_workbook
from openpyxl.styles import PatternFill, colors
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import Rule
from os import chdir


chdir(r'.\Chapter-12_Excel')

workbook = load_workbook(filename='reviews-sample.xlsx')

sheet = workbook.active

# conditional formatting
