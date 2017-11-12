import matplotlib.pyplot as plt
from pylab import rcParams
import pandas as pd
import seaborn as sns
import numpy as np


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
    # 1
    # sales_df = df[[x for x in df.columns if 'Sales' in x] + ['Year_of_Release']]
    # sales_df.groupby('Year_of_Release').sum().plot(kind='bar', rot=45)
    # 2
    # cols = ['Global_Sales', 'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count']
    # sns_plot = sns.pairplot(df[cols])
    # sns_plot.savefig('pairplot.png')
    # 3
    # sns.distplot(df.Critic_Score)
    # 4
    # top_platforms = df.Platform.value_counts().sort_values(ascending=False).head(5).index.values
    # sns.boxplot(y='Platform', x='Critic_Score', data=df[df.Platform.isin(top_platforms)], orient='h')
    # 5
    platform_genre_sales = df.pivot_table(index='Platform',
                                          columns='Genre',
                                          values='Global_Sales',
                                          aggfunc=sum).fillna(0).applymap(float)
    sns.heatmap(platform_genre_sales, annot=True, fmt='.1f', linewidths=.5)
    plt.show()


def test_telecom():
    print('Test Telecom Churn')
    df = pd.read_csv('../data/telecom_churn.csv')
    pd.set_option('display.width', 120)
    print(df.head())
    print('Shape : {}'.format(df.shape))
    # 1
    # df['Churn'].value_counts().plot(kind='bar', label='Churn')
    # 2
    # corr_matrix = df.drop(['State', 'International plan', 'Voice mail plan', 'Area code'], axis=1).corr()
    # sns.heatmap(corr_matrix)
    # 3
    features = list(set(df.columns) - set(['State', 'International plan', 'Voice mail plan', 'Area code',
                                           'Total day charge', 'Total eve charge', 'Total night charge',
                                           'Total intl charge', 'Churn']))
    # df[features].hist(figsize=(20, 12))
    # 4
    # sns.pairplot(df[features + ['Churn']], hue='Churn')
    # 5
    # print(len(features))
    # fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(16, 10))
    # for idx, feat in enumerate(features):
    #     sns.boxplot(x='Churn', y=feat, data=df, ax=axes[idx / 4, idx % 4])
    #     axes[idx / 4, idx % 4].legend()
    #     axes[idx / 4, idx % 4].set_xlabel('Churn')
    #     axes[idx / 4, idx % 4].set_ylabel(feat)
    # 6
    # _, axes = plt.subplots(1, 2, sharey=True, figsize=(16, 6))
    # sns.boxplot(x='Churn', y='Total day minutes', data=df, ax=axes[0])
    # sns.violinplot(x='Churn', y='Total day minutes', data=df, ax=axes[1])
    # 7
    # sns.countplot(x='Customer service calls', hue='Churn', data=df)
    # 8
    # _, axes = plt.subplots(1, 2, sharey=True, figsize=(16, 6))
    # sns.countplot(x='International plan', hue='Churn', data=df, ax=axes[0])
    # sns.countplot(x='Voice mail plan', hue='Churn', data=df, ax=axes[1])
    # 9
    print(df.groupby(['State'])['Churn'].agg([np.mean]).sort_values(by='mean', ascending=False).head())
    plt.show()


if __name__ == '__main__':
    rcParams['figure.figsize'] = 8, 5
    # test_seaborn_and_ploty()
    test_telecom()
