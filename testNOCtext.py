from grab import Grab

print('Grab text from temp_report.html')
g = Grab()
url_name = 'file://temp_report.html'
resp = g.go(url_name, charset='cp1251')
print('\nИтого портов:')
print('GPON:')
print('Монтировано: ', end='')
print(g.doc.rex_search(r'Итого(.|\n|\r|\s)*?GPON\s+(.+\n){2}.+\(([^<]+)\)\s+').group(3))
print('Активно: ', end='')
print(g.doc.rex_search(r'Итого(.|\n|\r|\s)*?GPON\s+(.+\n){4}.+\(([^<]+)\)\s+').group(3))
print('Задействовано: ', end='')
print(g.doc.rex_search(r'Итого(.|\n|\r|\s)*?GPON\s+(.+\n){6}.+\(([^<]+)\)\s+').group(3))
print('Свободно: ', end='')
print(g.doc.rex_search(r'Итого(.|\n|\r|\s)*?GPON\s+(.+\n){7}.+\s+([^<]+)\s+').group(3))
print('\nADSL:')
print('Монтировано:', end='')
print(g.doc.rex_search(r'Итого(.|\n|\r|\s)*?ADSL2\+\s+(.+\n){1}.+\s+([^<]+)\s+').group(3))
print('Активно: ', end='')
print(g.doc.rex_search(r'Итого(.|\n|\r|\s)*?ADSL2\+\s+(.+\n){3}.+\s+([^<]+)\s+').group(3))
print('Задействовано: ', end='')
print(g.doc.rex_search(r'Итого(.|\n|\r|\s)*?ADSL2\+\s+(.+\n){5}.+\s+([^<]+)\s+').group(3))
print('Свободно: ', end='')
print(g.doc.rex_search(r'Итого(.|\n|\r|\s)*?ADSL2\+\s+(.+\n){7}.+\s+([^<]+)\s+').group(3))
print('\nПортов на 1T3:', end='')
name_ats = ['31', '26']
for ats in name_ats:
    print('\nАТС ' + str(ats) + ':')
    print('Монтировано: ', end='')
    print(g.doc.rex_search(r'8202' + str(ats) + r'(.|\n|\r|\s)*?1T3(.|\n|\r|\s)*?GPON(.|\n|\r|\s)*?' +
                           r'summary(.*\n*){2}\s+\d+\(([^<]+)\)\s+').group(5))
    print('Активно: ', end='')
    print(g.doc.rex_search(r'8202' + str(ats) + r'(.|\n|\r|\s)*?1T3(.|\n|\r|\s)*?GPON(.|\n|\r|\s)*?' +
                           r'summary(.*\n*){4}\s+\d+\(([^<]+)\)\s+').group(5))
    print('Задействовано: ', end='')
    print(g.doc.rex_search(r'8202' + str(ats) + r'(.|\n|\r|\s)*?1T3(.|\n|\r|\s)*?GPON(.|\n|\r|\s)*?' +
                           r'summary(.*\n*){6}\s+\d+\(([^<]+)\)\s+').group(5))
    print('Свободно: ', end='')
    print(g.doc.rex_search(r'8202' + str(ats) + r'(.|\n|\r|\s)*?1T3(.|\n|\r|\s)*?GPON(.|\n|\r|\s)*?' +
                           r'summary(.*\n*){8}\s+(\d+)([^<]+)\s+').group(5))

print('\nTest:')


print('\n\nTHE END.')
