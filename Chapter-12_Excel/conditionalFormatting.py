from openpyxl import load_workbook
from openpyxl.formatting.rule import IconSetRule
from os import chdir

chdir(r'.\Chapter-12_Excel')

workbook = load_workbook(filename='reviews-sample.xlsx')
sheet = workbook.active

icon_rule = IconSetRule('5Arrows', 'num',[1, 2, 3, 4, 5])
sheet.conditional_formatting.add('H2:H100', icon_rule)

workbook.save('reviews-sample.xlsx')