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
    count = 0
    temp_row = None
    for row in rows:
        count += 1
        if row != temp_row:
            print('{} {} {} {}'.format(row.FAMILY, row.NAME, row.FARTHER, row.BIRTHDAY.strftime("%d.%m.%Y")))
        temp_row = row
    print('Count = {}'.format(count))
    cnxn.close()
