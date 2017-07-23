import testQTBD_model


def select_all_from_bd():
    return testQTBD_model.select_all_from_bd()


def select_from_db(family='', name='', farther='',
                   birthday_year='', birthday_month='', birthday_day='',
                   ksiva='', city='', selsovet='',
                   street='',house='', flat='',
                   zodiak=''):
    sql_request = ''
    return testQTBD_model.select_from_db(family, name, farther,
                                         birthday_year, birthday_month, birthday_day,
                                         ksiva, city, selsovet,
                                         street,house, flat,
                                         sql_request)


def main():
    print('Test controller')
    for row in testQTBD_model.select_all_from_bd():
        print(row)


if __name__ == '__main__':
    main()
