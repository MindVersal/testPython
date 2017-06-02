from openpyxl import Workbook

print('Test Excel Workbook.')
wb = Workbook()
ws = wb.active
ws['A1'] = 42
ws.append([1, 2, 3])
wb.save("temp/temp.xlsx")

print('\nTHE END.')
