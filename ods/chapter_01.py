import numpy as np
import pandas as pd


def detect_gender(pd):
    gender_1 = df[df['gender'] == 1]
    gender_2 = df[df['gender'] == 2]
    gender_1_mean_height = gender_1['height'].mean()
    gender_2_mean_height = gender_2['height'].mean()
    if gender_1_mean_height > gender_2_mean_height:
        gender_1_name = 'man'
        gender_2_name = 'women'
    else:
        gender_1_name = 'women'
        gender_2_name = 'men'
    print('Count ({}) gender == 1 : {}, mean height : {}'.
          format(gender_1_name, len(gender_1), gender_1_mean_height))
    print('Count ({}) gender == 2 : {}, mean height : {}'.
          format(gender_2_name, len(gender_2), gender_2_mean_height))


if __name__ == '__main__':
    df = pd.read_csv('../data/mlbootcamp5_train.csv', sep=';', index_col='id')
    pd.set_option('display.width', 100)
    print('DataFrame head: \n{}'.format(df.head()))
    print('DataFrame shape: {}'.format(df.shape))
    detect_gender(pd)
