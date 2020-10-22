from openpyxl import load_workbook
from openpyxl.styles import PatternFill, colors
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import Rule
from os import chdir


chdir(r'.\Chapter-12_Excel')

workbook = load_workbook(filename='reviews-sample.xlsx')
sheet = workbook.active

# conditional formatting cofigurations
red_backgroung = PatternFill(bgColor=colors.BLUE)
diff_style = DifferentialStyle(fill=red_backgroung)
rule = Rule(type='expression', dxf=diff_style)
rule.formula = ['$H1<3']

sheet.conditional_formatting.add(sheet.dimensions, rule)

workbook.save('reviews-sample.xlsx')