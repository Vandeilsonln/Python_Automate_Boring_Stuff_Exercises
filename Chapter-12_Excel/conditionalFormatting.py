import openpyxl
from openpyxl.chart import LineChart, Reference
from os import chdir
import random


chdir(r'.\Chapter-12_Excel')

workbook = openpyxl.Workbook()
sheet = workbook.active

# Let's create some sample sales data
rows = [
    ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    [1, ],
    [2, ],
    [3, ]
]

for i in rows:
    sheet.append(i)

for j in sheet.iter_rows(min_row=2, max_row=4, min_col=2, max_col=13):
    for cell in j:
        cell.value = random.randrange(2, 200)

chart = LineChart()
data = Reference(worksheet=sheet,
min_row=2, max_row=4, min_col=1, max_col=13)

chart.add_data(data, from_rows=True, titles_from_data=True)
sheet.add_chart(chart, 'C6')

cats = Reference(worksheet=sheet,
                 min_row=1,
                 max_row=1,
                 min_col=2,
                 max_col=13)

chart.set_categories(cats)
chart.x_axis.title = 'Months'
chart.y_axis.title = 'Sales (per unity)'

workbook.save('line_chart.xlsx')