import matplotlib.pylab as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import collections
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.externals.six import StringIO
import pydotplus
import math


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
    y = df_train[['Поедет']]
    df_train, df_test = intersect_features(train=df_train, test=df_test)
    print('DataFrame Train shape: {}'.format(df_train.shape))
    print('DataFrame Test shape: {}'.format(df_test.shape))
    go_tree_classifier = DecisionTreeClassifier(random_state=42)
    go_tree_classifier.fit(df_train.values, y.values)
    print(go_tree_classifier)
    print(df_train.values)
    print(y)
    dot_data = StringIO()
    export_graphviz(go_tree_classifier,
                    out_file=dot_data,
                    filled=True)
    graph_data = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph_data.write_pdf('../img/go_tree_classifier.pdf')
    # plt.show()


def entropy(a_list):
    counts = {}
    count_all = len(a_list)
    for i in a_list:
        if i in counts.keys():
            counts[i] += 1
        else:
            counts[i] = 1
    sum_entropy = 0
    for i in counts.keys():
        p = counts[i]/count_all
        sum_entropy -= p * math.log2(p)
    return sum_entropy


def information_gain(root, left, right):
    count_elements_in_root = len(root)
    count_elements_in_left = len(left)
    count_elements_in_right = len(right)
    entropy_left_and_right = (count_elements_in_left / count_elements_in_root) * entropy(left) + \
                             (count_elements_in_right / count_elements_in_root) * entropy(right)
    return entropy(root) - entropy_left_and_right


def calculate_entropy():
    print('Calculate entropy.')
    balls = [1 for i in range(9)] + [0 for i in range(11)]
    balls_left = [1 for i in range(8)] + [0 for i in range(5)]
    balls_right = [1 for i in range(1)] + [0 for i in range(6)]
    # print('Balls      : {}'.format(balls))
    # print('Balls left : {}'.format(balls_left))
    # print('Balls right: {}'.format(balls_right))
    print('Entropy balls      : {:.3f}'.format(entropy(balls)))
    print('Entropy balls_left : {:.3f}'.format(entropy(balls_left)))
    print('Entropy balls_right: {:.3f}'.format(entropy(balls_right)))
    print('Array [1,2,3,4,5,6]: {:.3f}'.format(entropy([1, 2, 3, 4, 5, 6])))
    print('Array []: {:.3f}'.format(entropy([])))
    print('Information gain (IG) = {:.3f}'.format(information_gain(balls, balls_left, balls_right)))


def analise_adult_dadaframe():
    data_train = pd.read_csv('../data/adult_train.csv', sep=';')
    print(data_train.head())


def last_end():
    print('The End')


if __name__ == '__main__':
    init_first()
    # test_adult()
    # calculate_entropy()
    analise_adult_dadaframe()
    last_end()
