# Program extracting first column 
import xlrd 
import json

loc = "data.xls"

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

state = set()
k = 0

for i in range(sheet.nrows): 
    print(sheet.cell_value(i, 5))
    print(sheet.cell_value(i, 9))
    state.add(sheet.cell_value(i, 5).strip())

print(state)

state_sales = {}
for s in state:
    state_sales[s] = 0

print(state_sales)

for i in range(sheet.nrows):
    state_sales[sheet.cell_value(i,5).strip()] += sheet.cell_value(i,9)

print(state_sales)