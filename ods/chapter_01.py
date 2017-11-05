import numpy as np
import pandas as pd


def detect_gender(df):
    gender_1 = df[df['gender'] == 1]
    gender_2 = df[df['gender'] == 2]
    gender_1_mean_height = gender_1['height'].mean()
    gender_2_mean_height = gender_2['height'].mean()
    if gender_1_mean_height > gender_2_mean_height:
        gender_1_name = 'men'
        gender_2_name = 'women'
    else:
        gender_1_name = 'women'
        gender_2_name = 'men'
    print('{} {} and {} {}'.
          format(len(gender_1), gender_1_name, len(gender_2), gender_2_name))


def detect_alcohol(pd):
    gender_1_name = 'women'
    gender_2_name = 'man'
    count_alcohol_gender_1 = df[df['gender'] == 1]['alco'].mean()
    count_alcohol_gender_2 = df[df['gender'] == 2]['alco'].mean()
    if count_alcohol_gender_1 > count_alcohol_gender_2:
        print('women')
    else:
        print('men')


if __name__ == '__main__':
    df = pd.read_csv('../data/mlbootcamp5_train.csv', sep=';', index_col='id')
    pd.set_option('display.width', 100)
    print('DataFrame head: \n{}'.format(df.head()))
    print('DataFrame shape: {}'.format(df.shape))
    print('How much women and men in DataFrame:')
    detect_gender(df)
    print('Who in mean write, what have alcohol: ')
    detect_alcohol(df)
