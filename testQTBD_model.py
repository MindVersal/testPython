import sqlalchemy


def select_all_from_bd():
    return select_from_db()


def select_from_db(familia='', name='', farther='',
                   birthday_year='', birthday_month='', birthday_day='',
                   ksiva='', city='', selsovet='',
                   street='',house='', flat='', sql_request=''):
    connector = (
        r'E:/BD/2005.db'
    )
    engine = sqlalchemy.create_engine(r'sqlite:///{}'.format(connector))
    # sql_count = """
    #                 SELECT COUNT (*) FROM {}
    #                 """
    sql_request = """
                        SELECT * 
                          FROM db2005
                          WHERE
                            NAME='АБУ'
                          ORDER BY FAMILY, NAME, FARTHER
                      """
    rows = engine.execute(sql_request)
    for row in rows:
        yield row


def main():
    print('I am finding all records in db...')
    print('I am find:')
    select_all_range = select_all_from_bd()
    for row in select_all_range:
        print(row)


if __name__ == '__main__':
    main()
