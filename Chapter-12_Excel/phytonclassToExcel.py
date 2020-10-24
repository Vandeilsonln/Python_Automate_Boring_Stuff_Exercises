from os import chdir
import random
from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference
from db_classes import Product, Sale

chdir('Chapter-12_Excel')

products = []

# Let's create 5 products
for i in range(1,6):
    sales = []

    # Create 5 months of sales
    for _ in range(5):
        sale = Sale(quantity=random.randrange(5,150))
        sales.append(sale)
    
    product = Product(id=str(i), name = 'Product %s' % i, sales=sales)
    products.append(product)


# Let's pass this info to a spreadsheet
workbook = Workbook()
sheet = workbook.active
sheet.title = 'sales'

# Append column names first
sheet.append(['Product ID', 'Product Name', 'Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5'])

# Append the data
for i in products:
    data = [i.id, i.name]
    for j in i.sales:
        data.append(j.quantity)
    sheet.append(data)

# Create a Chart
chart = LineChart()
data = Reference(worksheet=sheet, min_row=2, max_row=6, min_col=2, max_col=7)

chart.add_data(data, titles_from_data=True, from_rows=True)
sheet.add_chart(chart, 'B8')

# Categories
cats = Reference(worksheet=sheet, min_row=1, max_row=1, min_col=3, max_col=7)
chart.set_categories(cats)

# Create Axis
chart.x_axis.title = 'Months'
chart.y_axis.title = 'Sales (per unity)'

# Save the workbook
workbook.save('pythonToExcel.xlsx')