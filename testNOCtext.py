from grab import Grab
from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.styles import Alignment
from openpyxl.styles import Border
from openpyxl.styles import Side
import datetime

print('Grab text from temp_report.html')
g = Grab()
wb = Workbook()
ws = wb.active
url_name = r'file://temp\temp_report.html'
resp = g.go(url_name, charset='cp1251')
temp_row = []
ws['A1'] = 'Тип портов'
ws['B1'] = 'Монтировано портов'
ws['C1'] = 'Активных портов'
ws['D1'] = 'Задействовано портов'
ws['E1'] = 'Свободно портов'
temp_row.append('ADSL2+:')
temp_row.append(g.doc.rex_search(r'Итого(.|\n|\r|\s)*?ADSL2\+\s+(.+\n){1}.+\s+([^<]+)\s+').group(3))
temp_row.append(g.doc.rex_search(r'Итого(.|\n|\r|\s)*?ADSL2\+\s+(.+\n){3}.+\s+([^<]+)\s+').group(3))
temp_row.append(g.doc.rex_search(r'Итого(.|\n|\r|\s)*?ADSL2\+\s+(.+\n){5}.+\s+([^<]+)\s+').group(3))
temp_row.append(g.doc.rex_search(r'Итого(.|\n|\r|\s)*?ADSL2\+\s+(.+\n){7}.+\s+([^<]+)\s+').group(3))
ws.append(temp_row)
temp_row = []
temp_row.append('GPON:')
temp_row.append(g.doc.rex_search(r'Итого(.|\n|\r|\s)*?GPON\s+(.+\n){2}.+\(([^<]+)\)\s+').group(3))
temp_row.append(g.doc.rex_search(r'Итого(.|\n|\r|\s)*?GPON\s+(.+\n){4}.+\(([^<]+)\)\s+').group(3))
temp_row.append(g.doc.rex_search(r'Итого(.|\n|\r|\s)*?GPON\s+(.+\n){6}.+\(([^<]+)\)\s+').group(3))
temp_row.append(g.doc.rex_search(r'Итого(.|\n|\r|\s)*?GPON\s+(.+\n){7}.+\s+([^<]+)\s+').group(3))
ws.append(temp_row)
temp_row = []
ws.merge_cells('A7:B7')
ws.merge_cells('D7:E7')
ws['A7'] = 'Абонентов на 1T3 коструктивах'
ws['D7'] = 'Монтировано на 1T3 коструктивах'
ws['A8'] = 'АТС'
ws['B8'] = 'Кол-во абонентов'
ws['D8'] = 'АТС'
ws['E8'] = 'Кол-во портов'
name_ats = ['31', '26']
for ats in name_ats:
    temp_row = []
    temp_row.append('8202' + ats)
    temp_row.append(int(g.doc.rex_search(r'8202' + str(ats) + r'(.|\n|\r|\s)*?1T3(.|\n|\r|\s)*?GPON(.|\n|\r|\s)*?' +
                                         r'summary(.*\n*){6}\s+\d+\(([^<]+)\)\s+').group(5)))
    temp_row.append('')
    temp_row.append('8202' + ats)
    temp_row.append(int(g.doc.rex_search(r'8202' + str(ats) + r'(.|\n|\r|\s)*?1T3(.|\n|\r|\s)*?GPON(.|\n|\r|\s)*?' +
                                         r'summary(.*\n*){2}\s+\d+\(([^<]+)\)\s+').group(5)))
    ws.append(temp_row)
temp_row = []
temp_row.append('Итого: ')
temp_row.append('=SUM(B9:B10)')
temp_row.append('')
temp_row.append('Итого: ')
temp_row.append('=SUM(E9:E10)')
ws.append(temp_row)
temp_row = []
ws.merge_cells('A15:E15')
ws['A15'] = 'Абонентов на АТС 26'
ws['A16'] = 'OLT'
ws['B16'] = 'Монтировано портов'
ws['C16'] = 'Активных портов'
ws['D16'] = 'Задействовано портов'
ws['E16'] = 'Свободно портов'
name_olt = ['MA5680T-1', 'MA5680T-2', 'MA5680T-3', 'MA5680T-4', '1T3-1']
for olt in name_olt:
    temp_row = []
    temp_row.append(olt)
    temp_row.append(int(g.doc.rex_search(r'820226(.|\n|\r|\s)*?' + olt + '(.|\n|\r|\s)*?GPON(.|\n|\r|\s)*?' +
                                         r'summary(.*\n*){2}\s+\d+\(([^<]+)\)\s+').group(5)))
    temp_row.append(int(g.doc.rex_search(r'820226(.|\n|\r|\s)*?' + olt + '(.|\n|\r|\s)*?GPON(.|\n|\r|\s)*?' +
                                         r'summary(.*\n*){4}\s+\d+\(([^<]+)\)\s+').group(5)))
    temp_row.append(int(g.doc.rex_search(r'820226(.|\n|\r|\s)*?' + olt + '(.|\n|\r|\s)*?GPON(.|\n|\r|\s)*?' +
                                         r'summary(.*\n*){6}\s+\d+\(([^<]+)\)\s+').group(5)))
    temp_row.append(int(g.doc.rex_search(r'820226(.|\n|\r|\s)*?' + olt + '(.|\n|\r|\s)*?GPON(.|\n|\r|\s)*?' +
                                         r'summary(.*\n*){8}\s+(\d+)\s+').group(5)))
    ws.append(temp_row)
temp_row = []
temp_row.append('Итого: ')
temp_row.append('=SUM(B17:B21)')
temp_row.append('=SUM(C17:C21)')
temp_row.append('=SUM(D17:D21)')
temp_row.append('=SUM(E17:E21)')
ws.append(temp_row)
temp_row = []
styleAlignment = Alignment(horizontal='center')
styleTextBold = Font(bold=True)
styleBorder = Border(
    left=Side(border_style='thin', color='FF000000'),
    right=Side(border_style='thin', color='FF000000'),
    top=Side(border_style='thin', color='FF000000'),
    bottom=Side(border_style='thin', color='FF000000')
)
styleNoBorder = Border(
    left=Side(border_style='thin', color='FF000000'),
    right=Side(border_style='thin', color='FF000000'),
    top=Side(border_style=None, color='FF000000'),
    bottom=Side(border_style=None, color='FF000000')
)
cells_bold = ['A1', 'B1', 'C1', 'D1', 'E1', 'A7', 'D7', 'A8', 'B8', 'D8', 'E8',
              'A11', 'B11', 'D11', 'E11', 'A15', 'A16', 'B16', 'C16', 'D16', 'E16',
              'A22', 'A22', 'B22', 'C22', 'D22', 'E22']
for cell in cells_bold:
    ws[cell].font = styleTextBold
    ws[cell].alignment = styleAlignment
    ws[cell].border = styleBorder

cols = ['A', 'B', 'C', 'D', 'E']
for col in cols:
    for row in range(2, 4):
        ws[col+str(row)].alignment = styleAlignment
        ws[col + str(row)].border = styleBorder
    for row in range(9, 11):
        ws[col+str(row)].alignment = styleAlignment
        ws[col + str(row)].border = styleBorder
    for row in range(17, 22):
        ws[col+str(row)].alignment = styleAlignment
        ws[col + str(row)].border = styleBorder
border_manual = ['B7', 'E7', 'B15', 'C15', 'D15', 'E15']
for cell in border_manual:
    ws[cell].border = styleBorder
ws['C9'].border = styleNoBorder
ws['C10'].border = styleNoBorder
ws.column_dimensions['A'].width = 11
ws.column_dimensions['B'].width = 20
ws.column_dimensions['C'].width = 16
ws.column_dimensions['D'].width = 21
ws.column_dimensions['E'].width = 17

month_year = datetime.datetime.now().strftime('%d%m%y')
wb.save('temp/report_' + month_year + '.xlsx')

print('\nTHE END.')
