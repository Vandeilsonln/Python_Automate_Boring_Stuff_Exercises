from os import chdir
import random
from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference
from db_classes import Product, Sale


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

