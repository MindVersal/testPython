import pyodbc


def main():
    print('Main Test.')


if __name__ == '__main__':
    main()
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=E:\BD\2005.accdb;'
    )
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    rows = crsr.execute("""
                          SELECT * 
                            FROM 2005  
                            WHERE 
                              NAME='АБУ'
                            ORDER BY FAMILY, NAME, FARTHER, BIRTHDAY, KSIVA, CITY, SELSOVET, STREET, HOUSE, FLAT
                        """)
    count_all = 0
    count_allow = 0
    temp_row = None
    for row in rows:
        count_all += 1

        if row != temp_row:
            print('{} {} {} {}'.format(row.FAMILY, row.NAME, row.FARTHER, row.BIRTHDAY.strftime("%d.%m.%Y")))
            count_allow += 1
        temp_row = row
    print('Count: allow/all = {}/{}'.format(count_allow, count_all))
    cnxn.close()
