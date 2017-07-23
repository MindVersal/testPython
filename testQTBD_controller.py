import testQTBD_model


def select_all_from_bd():
    return testQTBD_model.select_all_from_bd()


def select_from_db(family='', name='', farther='',
                   birthday_year='', birthday_month='', birthday_day='',
                   ksiva='', city='', selsovet='',
                   street='', house='', flat='',
                   zodiak='', interactive=True):
    sql_request_start = """
                          SELECT * 
                            FROM db2005 
                        """
    sql_request_where = """ WHERE """
    # sql_request_where = """
    #                     WHERE NAME LIKE 'АБУ%'
    #                   """
    no_first_where_in_sql = False
    #
    # Знак Зодиака 	Дата рождения
    #
    # Овен 	        21.03 - 20.04
    # Телец 	    21.04 - 21.05
    # Близнецы 	    22.05 - 21.06
    # Рак 	        22.06 - 22.07
    # Лев 	        23.07 - 21.08
    # Дева 	        22.08 - 23.09
    # Весы 	        24.09 - 23.10
    # Скорпион 	    24.10 - 22.11
    # Стрелец 	    23.11 - 22.12
    # Козерог 	    23.12 - 20.01
    # Водолей 	    21.01 - 19.02
    # Рыбы 	        20.02 - 20.03
    #
    zodiak_dates_months = {'': '',
                           'ОВЕН': '03-04',
                           'ТЕЛЕЦ': '04-05',
                           'БЛИЗНЕЦЫ': '05-06',
                           'РАК': '06-07',
                           'ЛЕВ': '07-08',
                           'ДЕВА': '08-09',
                           'ВЕСЫ': '09-10',
                           'СКОРПИОН': '10-11',
                           'СТРЕЛЕЦ': '11-12',
                           'КОЗЕРОГ': '12-01',
                           'ВОДОЛЕЙ': '01-02',
                           'РЫБЫ': '02-03'}
    zodiak_dates_days = {'': '',
                         'ОВЕН': '21-20',
                         'ТЕЛЕЦ': '21-21',
                         'БЛИЗНЕЦЫ': '22-21',
                         'РАК': '22-22',
                         'ЛЕВ': '23-21',
                         'ДЕВА': '22-23',
                         'ВЕСЫ': '24-23',
                         'СКОРПИОН': '24-22',
                         'СТРЕЛЕЦ': '23-22',
                         'КОЗЕРОГ': '23-20',
                         'ВОДОЛЕЙ': '21-19',
                         'РЫБЫ': '20-20'}
    if family != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        if interactive:
            sql_request_where += """ (FAMILY LIKE '""" + family.upper() + """%') """
        else:
            sql_request_where += """ (FAMILY='""" + family.upper() + """') """
    if name != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        if interactive:
            sql_request_where += """ (NAME LIKE '""" + name.upper() + """%')"""
        else:
            sql_request_where += """ (NAME='""" + name.upper() + """')"""
    if farther != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        if interactive:
            sql_request_where += """ (FARTHER LIKE '""" + farther.upper() + """%')"""
        else:
            sql_request_where += """ (FARTHER='""" + farther.upper() + """')"""
    if birthday_year != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        sql_request_where += """ (BIRTHDAY='""" + birthday_year.upper() + """')"""
    if birthday_month != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        sql_request_where += """ (BIRTHDAY_MONTH='""" + birthday_month.upper() + """')"""
    if birthday_day != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        sql_request_where += """ (BIRTHDAY_DAY='""" + birthday_day.upper() + """')"""
    if ksiva != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        if interactive:
            sql_request_where += """ (KSIVA LIKE '%""" + ksiva.upper() + """%')"""
        else:
            sql_request_where += """ (KSIVA='""" + ksiva.upper() + """')"""
    if city != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        if interactive:
            sql_request_where += """ (CITY LIKE '""" + city.upper() + """%')"""
        else:
            sql_request_where += """ (CITY='""" + city.upper() + """')"""
    if selsovet != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        if interactive:
            sql_request_where += """ (SELSOVET LIKE '%""" + selsovet.upper() + """%')"""
        else:
            sql_request_where += """ (SELSOVET='""" + selsovet.upper() + """')"""
    if street != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        if interactive:
            sql_request_where += """ (STREET LIKE '%""" + street.upper() + """%')"""
        else:
            sql_request_where += """ (STREET='""" + street.upper() + """')"""
    if house != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        sql_request_where += """ (STREET='""" + house.upper() + """')"""
    if flat != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        sql_request_where += """ (STREET='""" + flat.upper() + """')"""

    sql_request = sql_request_start + sql_request_where
    return testQTBD_model.select_from_db(sql_request=sql_request)


def main():
    print('Test controller')
    for row in testQTBD_model.select_all_from_bd():
        print(row)


if __name__ == '__main__':
    main()
