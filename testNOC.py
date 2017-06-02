from grab import Grab

print('Test NOC DB')
url_name_login = 'http://10.166.0.27/db/index.php'
url_name_report = 'http://10.166.0.27/db/index.php?a=repAdmin&c=sendForm&r=equipInventory&id_pop=3533&id_equip_type=&id_port_type='
g = Grab(timeout=100, connect_timeout=20)
g.go(url_name_login)
g.doc.set_input('login', 'pia@ex.tchercom.ru')
print('Insert password:')
password = input()
g.doc.set_input('password', password)
g.doc.submit()
resp = g.go(url_name_report)
resp.charset = 'cp1251'
open('./temp/temp_report.html', 'w').write(resp.unicode_body())

print('\n\nTHE END.')
