import sqlalchemy
import os
import pyodbc
import pyprind


def test_db(engine_test, db_name):
    print('Test db: {}'.format(db_name))
    rows_recipient = engine_test.execute("""SELECT * FROM {}""".format(db_name))
    for row in rows_recipient:
        print(row)


def main():
    print('Main Test.')
    connector_donor = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=E:\BD\2005.accdb;'
    )
    connector_recipient = (
        r'E:/BD/2005.db'
    )
    engine_donor = pyodbc.connect(connector_donor)
    cursor_donor = engine_donor.cursor()
    if os.path.exists(connector_recipient):
        os.remove(connector_recipient)
    engine_recipient = sqlalchemy.create_engine(r'sqlite:///{}'.format(connector_recipient))
    sql_request = """
                  SELECT * 
                    FROM 2005  
                    WHERE 
                      NAME='ИННОКЕНТИЙ'
                    ORDER BY FAMILY, NAME, FARTHER, BIRTHDAY, KSIVA, CITY, SELSOVET, STREET, HOUSE, FLAT
                 """
    sql_schema = """
                  CREATE TABLE db2005 (
                    FAMILY varchar,
                    NAME varchar,
                    FARTHER varchar,
                    BIRTHDAY_YEAR varchar,
                    BIRTHDAY_MONTH varchar,
                    BIRTHDAY_DAY varchar,
                    KSIVA varchar,
                    CITY varchar,
                    SELSOVET varchar,
                    STREET varchar,
                    HOUSE varchar,
                    FLAT varchar
                  );
                 """
    sql_insert = """
                    INSERT INTO db2005
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                 """
    sql_count = """
                SELECT COUNT (*) FROM {}
                """
    cursor_donor.execute(sql_count.format(r'2005'))
    rowcount = cursor_donor.fetchone()[0]
    rows_donor = engine_donor.execute(sql_request)
    engine_recipient.execute(sql_schema)
    count_all = 0
    count_allow = 0
    temp_row = None
    bar = pyprind.ProgBar(245)
    for row in rows_donor:
        bar.update()
        count_all += 1
        if row != temp_row:
            row_family = row.FAMILY.upper() if row.FAMILY is not None else '0'
            row_name = row.NAME.upper() if row.NAME is not None else '0'
            row_farther = row.FARTHER.upper() if row.FARTHER is not None else '0'
            row_birthday_year = row.BIRTHDAY.strftime('%Y') if row.BIRTHDAY is not None else '0'
            row_birthday_month = row.BIRTHDAY.strftime('%m') if row.BIRTHDAY is not None else '0'
            row_birthday_day = row.BIRTHDAY.strftime('%d') if row.BIRTHDAY is not None else '0'
            row_ksiva = row.KSIVA.upper() if row.KSIVA is not None else '0'
            row_city = row.CITY.upper() if row.CITY is not None else '0'
            row_selsovet = row.SELSOVET.upper() if row.SELSOVET is not None else '0'
            row_street = row.STREET.upper() if row.STREET is not None else '0'
            row_house = row.HOUSE.upper() if row.HOUSE is not None else '0'
            row_flat = str(row.FLAT).upper() if row.FLAT is not None else '0'
            engine_recipient.execute(sql_insert, row_family, row_name, row_farther, row_birthday_year,
                                     row_birthday_month, row_birthday_day, row_ksiva, row_city,
                                     row_selsovet, row_street, row_house, row_flat)
            count_allow += 1
        temp_row = row
    print('Count: read/all = {}/{}'.format(count_all, rowcount))
    print('Count read: allow/all = {}/{}'.format(count_allow, count_all))
    cursor_donor.close()
    # test_db(engine_recipient, r'db2005')


if __name__ == '__main__':
    main()
