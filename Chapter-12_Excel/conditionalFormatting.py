from openpyxl import load_workbook
from openpyxl.styles import PatternFill
from openpyxl.styles.colors import Color
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import Rule
from openpyxl.formatting.rule import ColorScaleRule
from os import chdir


chdir(r'.\Chapter-12_Excel')

workbook = load_workbook(filename='reviews-sample.xlsx')
sheet = workbook.active

# conditional formatting color scale
color_scale_rule = ColorScaleRule(start_type='min', start_color=Color(indexed=37), end_type='max', end_color=Color(indexed=58))

sheet.conditional_formatting.add('H2:H100', color_scale_rule)

# conditional formatting color scale 3 colors
# color_scale_rule = ColorScaleRule(start_value=1, start_color=Color(indexed=2), mid_value=3, mid_color=Color(indexed=43) , end_value=5, end_color=Color(indexed=17))
# sheet.conditional_formatting.add('H2:H100', color_scale_rule)

sheet.auto_filter.ref = 'H1:H100'

workbook.save('reviews-sample.xlsx')