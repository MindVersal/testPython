from pylab import rcParams
import pandas as pd
import seaborn as sns


def test_seaborn_and_ploty():
    print('Test Seaborn and Ploty.')
    df = pd.read_csv('../data/video_games_sales.csv')
    pd.set_option('display.width', 160)
    df.dropna(inplace=True)
    df['User_Score'] = df.User_Score.astype('float64')
    df['Year_of_Release'] = df.Year_of_Release.astype('int64')
    df['User_Count'] = df.User_Count.astype('int64')
    df['Critic_Count'] = df.Critic_Count.astype('int64')
    print(df.shape)
    userful_cols = ['Name', 'Platform', 'Year_of_Release', 'Genre',
                    'Global_Sales', 'Critic_Score', 'Critic_Count',
                    'User_Score', 'User_Count', 'Rating'
                    ]
    print(df[userful_cols].head())


if __name__ == '__main__':
    rcParams['figure.figsize'] = 8, 5
    test_seaborn_and_ploty()
