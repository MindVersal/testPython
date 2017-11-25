import matplotlib.pylab as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import collections
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def init_first():
    print('Homework for chapter 03')


def create_df(dic, feature_list):
    out = pd.DataFrame(dic)
    out = pd.concat([out, pd.get_dummies(out[feature_list])], axis=1)
    out.drop(feature_list, axis=1, inplace=True)
    return out


# Некоторые значения признаков есть в тесте, но нет в трейне и наоборот
def intersect_features(train, test):
    common_feat = list(set(train.keys()) & set(test.keys()))
    return train[common_feat], test[common_feat]


def create_train(df_train, features):
    df_train['Внешность'] = ['приятная', 'приятная', 'приятная', 'отталкивающая',
                             'отталкивающая', 'отталкивающая', 'приятная']
    df_train['Алкоголь_в_напитке'] = ['да', 'да', 'нет', 'нет', 'да', 'да', 'да']
    df_train['Уровень_красноречия'] = ['высокий', 'низкий', 'средний', 'средний', 'низкий',
                                       'высокий', 'средний']
    df_train['Потраченные_деньги'] = ['много', 'мало', 'много', 'мало', 'много',
                                      'много', 'много']
    df_train['Поедет'] = LabelEncoder().fit_transform(['+', '-', '+', '-', '-', '+', '+'])
    return create_df(df_train, features)


def create_test(df_test, features):
    df_test['Внешность'] = ['приятная', 'приятная', 'отталкивающая']
    df_test['Алкоголь_в_напитке'] = ['нет', 'да', 'да']
    df_test['Уровень_красноречия'] = ['средний', 'высокий', 'средний']
    df_test['Потраченные_деньги'] = ['много', 'мало', 'много']
    return create_df(df_test, features)


def test_adult():
    features = ['Внешность', 'Алкоголь_в_напитке', 'Уровень_красноречия', 'Потраченные_деньги']
    df_train = {}
    df_train = create_train(df_train, features)
    df_test = {}
    df_test = create_test(df_test, features)
    print('DataFrame Train shape: {}'.format(df_train.shape))
    print('DataFrame Test shape: {}'.format(df_test.shape))
    y = df_train['Поедет']
    df_train, df_test = intersect_features(train=df_train, test=df_test)
    print('DataFrame Train shape: {}'.format(df_train.shape))
    print('DataFrame Test shape: {}'.format(df_test.shape))
    print(df_train)
    # plt.show()


def last_end():
    print('The End')


if __name__ == '__main__':
    init_first()
    test_adult()
    last_end()
