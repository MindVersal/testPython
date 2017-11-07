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
    df.insert(loc=len(df.columns), column='age_years', value=round(df['age'] / 365))
    smoking_men_age_60_64 = df[(df['gender'] == 2) & (df['age_years'] >= 60) & (df['age_years'] <= 64)]
    # 1 => 4; 2 => 5-7; 3 => 8;
    smoking_men_age_60_64_and_ap_120_and_chol_4 = \
        smoking_men_age_60_64[(smoking_men_age_60_64['ap_hi'] < 120) &
                              (smoking_men_age_60_64['cholesterol'] == 1)]
    smoking_men_age_60_64_and_ap_160_180_and_chol_8 = \
        smoking_men_age_60_64[(smoking_men_age_60_64['ap_hi'] >= 160) &
                              (smoking_men_age_60_64['ap_hi'] < 180) &
                              (smoking_men_age_60_64['cholesterol'] == 3)]
    print(round(smoking_men_age_60_64_and_ap_120_and_chol_4['age'].count() /
                smoking_men_age_60_64_and_ap_160_180_and_chol_8['age'].count()))


def test_bmi(df):
    df.insert(loc=len(df.columns), column='bmi', value=round(df['weight'] / pow((df['height'] / 100), 2)))
    mean_bmi_for_all = round(df['bmi'].mean())
    print('Mean BMI for all in DataFrame: {}'.format(mean_bmi_for_all))
    print(18.5 <= mean_bmi_for_all <= 25)
    mean_bmi_for_women = round(df[df['gender'] == 1]['bmi'].mean())
    mean_bmi_for_men = round(df[df['gender'] == 2]['bmi'].mean())
    print('Mean BMI for women (gender == 1): {}'.format(mean_bmi_for_women))
    print('Mean BMI for men (gender == 2): {}'.format(mean_bmi_for_men))
    print(mean_bmi_for_women > mean_bmi_for_men)
    mean_bmi_for_sicking = round(df[df['cardio'] == 1]['bmi'].mean())
    mean_bmi_for_no_sicking = round(df[df['cardio'] == 0]['bmi'].mean())
    print('Mean BMI for cardio = 0: {}'.format(mean_bmi_for_no_sicking))
    print('Mean BMI for cardio = 1: {}'.format(mean_bmi_for_sicking))
    print(mean_bmi_for_no_sicking > mean_bmi_for_sicking)
    mean_bmi_for_no_sicking_and_no_alco_men = round(df[(df['gender'] == 2) &
                                                       (df['cardio'] == 0) &
                                                       (df['alco'] == 0)]['bmi'].mean())
    mean_bmi_for_no_sicking_and_no_alco_women = round(df[(df['gender'] == 1) &
                                                         (df['cardio'] == 0) &
                                                         (df['alco'] == 0)]['bmi'].mean())
    print('Mean no sicking and no alcohol men: {}'.format(mean_bmi_for_no_sicking_and_no_alco_men))
    print('Mean no sicking and no alcohol women: {}'.format(mean_bmi_for_no_sicking_and_no_alco_women))
    print(abs((((25 - 18.5) / 2) - mean_bmi_for_no_sicking_and_no_alco_men)) <
          abs((((25 - 18.5) / 2) - mean_bmi_for_no_sicking_and_no_alco_women)))


def count_percent_after_clear_df(df):
    count_all_rows = df['age'].count()
    df = df[df['ap_lo'] < df['ap_hi']]
    quantil_025_of_height_in_df = df['height'].quantile(.025)
    quantil_975_of_height_in_df = df['height'].quantile(.975)
    df = df[(df['height'] >= quantil_025_of_height_in_df) & (df['height'] <= quantil_975_of_height_in_df)]
    quantil_025_of_weight_in_df = df['weight'].quantile(.025)
    quantil_975_of_weight_in_df = df['weight'].quantile(.975)
    df = df[(df['weight'] >= quantil_025_of_weight_in_df) & (df['weight'] <= quantil_975_of_weight_in_df)]
    count_rows_after_clearing = df['age'].count()
    print(round(((count_all_rows - count_rows_after_clearing) / count_all_rows) * 100))


if __name__ == '__main__':
    df = pd.read_csv('../data/mlbootcamp5_train.csv', sep=';', index_col='id')
    pd.set_option('display.width', 120)
    print('DataFrame head: \n{}'.format(df.head()))
    print('DataFrame shape: {}'.format(df.shape))
    print('\nAnswering on questions.\n')
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
    print('6. Test Body Mass Index: ')
    test_bmi(df)
    print('7. How many percent get out after clearing.')
    count_percent_after_clear_df(df)
