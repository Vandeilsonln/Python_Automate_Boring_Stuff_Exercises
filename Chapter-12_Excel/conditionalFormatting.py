from openpyxl import load_workbook
from openpyxl.formatting.rule import DataBarRule
from openpyxl.styles.colors import Color
from os import chdir

chdir(r'.\Chapter-12_Excel')

workbook = load_workbook(filename='reviews-sample.xlsx')
sheet = workbook.active

data_bar_rule = DataBarRule(start_type='num', start_value=1,end_type='num', end_value=5, color=Color(indexed=17))
sheet.conditional_formatting.add('H2:H100', data_bar_rule)

workbook.save('reviews-sample.xlsx')