import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler


def test_hw_ch_02():
    print('Testing')
    train = pd.read_csv('../data/mlbootcamp5_train.csv', sep=';', index_col='id')
    print('Shape dataset: {}'.format(train.shape))
    print(train.head())
    # train_uniques = pd.melt(frame=train, value_vars=['gender', 'cholesterol',
    #                                                  'gluc', 'smoke', 'alco',
    #                                                  'active'],
    #                         id_vars=['cardio'])
    # train_uniques = pd.DataFrame(train_uniques.groupby(['variable', 'value', 'cardio'])['value'].count())\
    #     .sort_index(level=[0, 1])\
    #     .rename(columns={'value': 'count'})\
    #     .reset_index()
    # sns.factorplot(x='variable', y='count',
    #                hue='value', col='cardio',
    #                data=train_uniques,
    #                kind='bar', size=9)
    # for c in train.columns:
    #     n = train[c].nunique()
    #     print(c)
    #     if n <= 3:
    #         print(n, sorted(train[c].value_counts().to_dict().items()))
    #     else:
    #         print(n)
    #     print(10 * '-')
    print('Answer on question 1:')
    # sns.heatmap(data=train.corr())
    print('Height, Smoke')
    print('Answer on question 2:')
    # sns.violinplot(x='gender', y='height', hue='gender', scale='count', data=train)
    # _, axes = plt.subplots(1, 2, figsize=(16, 6))
    # sns.kdeplot(train[train['gender'] == 1]['height'], ax=axes[0])
    # sns.kdeplot(train[train['gender'] == 2]['height'], ax=axes[1])
    print('Gender 1 == Women, Gender 1 == Men')
    print('Answer on question 3:')
    scaler = StandardScaler()
    X = train.drop(['cardio'], axis=1)
    X.dropna(inplace=True)
    X_scaled = scaler.fit_transform(X)
    tsne = TSNE(random_state=42)
    # tsne_representation = tsne.fit_transform(X_scaled)
    # plt.scatter(tsne_representation[:, 0], tsne_representation[:, 1],
    #             c=train['cardio'].map({0: 'green', 1: 'red'}))
    # sns.pairplot(train, hue='cardio')
    print('Answer on question 5:')
    train['age_years'] = (train['age'] // 365.25).astype(int)
    # sns.countplot(x='age_years', hue='cardio', data=train)
    print('53')
    plt.show()


if __name__ == '__main__':
    sns.set_context('notebook',
                    font_scale=1.5,
                    rc={'figure.figsize': (12, 9),
                        'axes.titlesize': 18})
    # pd.set_option('display.width', 120)
    test_hw_ch_02()
