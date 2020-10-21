from openpyxl import load_workbook
from openpyxl.utils import FORMULAE
from os import chdir


chdir(r'.\Chapter-12_Excel')

def print_rows(CurSheet):
    for i in CurSheet.iter_rows(values_only=True):
        print(i)

workbook = load_workbook(filename='example.xlsx')

sheet = workbook.active

sheet.auto_filter.ref= sheet.dimensions
workbook.save(filename='example.xlsx')

# column test is "G"
sheet['G502'] = '=COUNTA(G2:G501)'
workbook.save(filename='example.xlsx')

