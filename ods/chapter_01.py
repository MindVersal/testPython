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


def detect_alcohol(df):
    gender_1_name = 'women'
    gender_2_name = 'man'
    mean_alcohol_gender_1 = df[df['gender'] == 1]['alco'].mean()
    mean_alcohol_gender_2 = df[df['gender'] == 2]['alco'].mean()
    if mean_alcohol_gender_1 > mean_alcohol_gender_2:
        print('women')
    else:
        print('men')


def percent_smoking(df):
    gender_1_name = 'women'
    gender_2_name = 'men'
    mean_smoking_gender_1 = df[df['gender'] == 1]['smoke'].mean()
    mean_smoking_gender_2 = df[df['gender'] == 2]['smoke'].mean()
    print(round(mean_smoking_gender_2 / mean_smoking_gender_1))


def mean_between_smoking_ans_no_smoking(df):
    mean_smoking = df[df['smoke'] == 1]['age'].mean()
    mean_no_smoking = df[df['smoke'] == 0]['age'].mean()
    print(round((mean_no_smoking - mean_smoking) / 30))


def between_sick_and_no_sick_humans(df):
    print('Do it')


if __name__ == '__main__':
    df = pd.read_csv('../data/mlbootcamp5_train.csv', sep=';', index_col='id')
    pd.set_option('display.width', 100)
    print('DataFrame head: \n{}'.format(df.head()))
    print('DataFrame shape: {}'.format(df.shape))
    print('1. How much women and men in DataFrame:')
    detect_gender(df)
    print('2. Who in mean write, what have alcohol: ')
    detect_alcohol(df)
    print('3. Count percent smoking is biggest men of women:')
    percent_smoking(df)
    print('4. How much month between smoking and no smoking.')
    mean_between_smoking_ans_no_smoking(df)
    print('5. How much count between sick and no sick humans: ')
    between_sick_and_no_sick_humans(df)
