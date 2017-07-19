import sqlalchemy


def main():
    connector = (
        r'E:/BD/2005.db'
    )
    engine = sqlalchemy.create_engine(r'sqlite:///{}'.format(connector))
    sql_request = """
                    SELECT * 
                      FROM db2005
                      WHERE
                        NAME='АБУ'
                      ORDER BY FAMILY, NAME, FARTHER
                  """
    rows = engine.execute(sql_request)
    for row in rows:
        print(' '.join(row))


if __name__ == '__main__':
    main()