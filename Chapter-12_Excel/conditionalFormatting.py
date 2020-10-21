from openpyxl import load_workbook
from openpyxl.utils import FORMULAE
from os import chdir


chdir(r'.\Chapter-12_Excel')

workbook = load_workbook(filename='reviews-sample.xlsx')