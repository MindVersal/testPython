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
    pd.set_option('display.width', 220)


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
    data_test = pd.read_csv('../data/adult_test.csv', sep=';')
    data_test = data_test[(data_test['Target'] == ' >50K.') | (data_test['Target'] == ' <=50K.')]
    data_train.at[data_train['Target'] == ' <=50K', 'Target'] = 0
    data_train.at[data_train['Target'] == ' >50K', 'Target'] = 1
    data_test.at[data_test['Target'] == ' <=50K.', 'Target'] = 0
    data_test.at[data_test['Target'] == ' >50K.', 'Target'] = 1
    # print(data_test.describe(include='all').T)

    # fig = plt.figure(figsize=(25, 15))
    # cols =5
    # rows = np.ceil(float(data_train.shape[1]) / cols)
    # for i, column in enumerate(data_train.columns):
    #     ax = fig.add_subplot(rows, cols, i + 1)
    #     ax.set_title(column)
    #     if data_train.dtypes[column] == np.object:
    #         data_train[column].value_counts().plot(kind='bar', axes=ax)
    #     else:
    #         data_train[column].hist(axes=ax)
    #         plt.xticks(rotation='vertical')
    # plt.subplots_adjust(hspace=0.7, wspace=0.2)

    # print('\nCounts: \n{}'.format(data_train['Target'].value_counts()))
    # print(data_test.head())
    data_test['Age'] = data_test['Age'].astype(np.int64)
    data_test['fnlwgt'] = data_test['fnlwgt'].astype(np.int64)
    data_test['Education_Num'] = data_test['Education_Num'].astype(np.int64)
    data_test['Capital_Gain'] = data_test['Capital_Gain'].astype(np.int64)
    data_test['Capital_Loss'] = data_test['Capital_Loss'].astype(np.int64)
    data_test['Hours_per_week'] = data_test['Hours_per_week'].astype(np.int64)
    # print(data_test.dtypes)

    categorical_columns_train = [c for c in data_train.columns if data_train[c].dtype.name == 'object']
    numerical_columns_train = [c for c in data_train.columns if data_train[c].dtype.name != 'object']
    categorical_columns_test = [c for c in data_test.columns if data_test[c].dtype.name == 'object']
    numerical_columns_test = [c for c in data_test.columns if data_test[c].dtype.name != 'object']
    # print('Categorical columns train: {}'.format(categorical_columns_train))
    # print('Categorical columns test:  {}'.format(categorical_columns_test))
    # print('Numerical columns train: {}'.format(numerical_columns_train))
    # print('Numerical columns test   {}'.format(numerical_columns_test))
    for c in categorical_columns_train:
        data_train[c] = data_train[c].fillna(data_train[c].mode())
    for c in categorical_columns_test:
        data_test[c] = data_test[c].fillna(data_test[c].mode())
    for c in numerical_columns_train:
        data_train[c] = data_train[c].fillna(data_train[c].median())
    for c in numerical_columns_test:
        data_test[c] = data_test[c].fillna(data_test[c].median())
    print()
    data_train = pd.concat([data_train,
                            pd.get_dummies(data_train['Workclass'], prefix='Workclass'),
                            pd.get_dummies(data_train['Education'], prefix='Education'),
                            pd.get_dummies(data_train['Martial_Status'], prefix='Martial_Status'),
                            pd.get_dummies(data_train['Occupation'], prefix='Occupation'),
                            pd.get_dummies(data_train['Relationship'], prefix='Relationship'),
                            pd.get_dummies(data_train['Race'], prefix='Race'),
                            pd.get_dummies(data_train['Sex'], prefix='Sex'),
                            pd.get_dummies(data_train['Country'], prefix='Country')
                            ], axis=1)
    data_test = pd.concat([data_test,
                           pd.get_dummies(data_test['Workclass'], prefix='Workclass'),
                           pd.get_dummies(data_test['Education'], prefix='Education'),
                           pd.get_dummies(data_test['Martial_Status'], prefix='Martial_Status'),
                           pd.get_dummies(data_test['Occupation'], prefix='Occupation'),
                           pd.get_dummies(data_test['Relationship'], prefix='Relationship'),
                           pd.get_dummies(data_test['Race'], prefix='Race'),
                           pd.get_dummies(data_test['Sex'], prefix='Sex'),
                           pd.get_dummies(data_test['Country'], prefix='Country')
                           ], axis=1)
    data_train.drop(['Workclass', 'Education', 'Martial_Status', 'Occupation',
                     'Relationship', 'Race', 'Sex', 'Country'],
                    axis=1, inplace=True)
    data_test.drop(['Workclass', 'Education', 'Martial_Status', 'Occupation',
                    'Relationship', 'Race', 'Sex', 'Country'],
                   axis=1, inplace=True)
    # print(data_test.describe(include='all').T)
    # print(set(data_train.columns) - set(data_test.columns))
    data_test['Country_ Holand-Netherlands'] = np.zeros([data_test.shape[0], 1])
    # print(set(data_train.columns) - set(data_test.columns))
    X_train = data_train.drop(['Target'], axis=1)
    y_train = data_train['Target']
    X_test = data_test.drop(['Target'], axis=1)
    y_test = data_test['Target']

    tree = DecisionTreeClassifier(random_state=17, max_depth=3)
    tree.fit(X_train, y_train)
    tree_predictions = tree.predict(X_test)
    print('Accuracy: {}'.format(accuracy_score(y_test, tree_predictions)))
    tree_params = {'max_depth': range(2, 11)}
    locally_best_tree = GridSearchCV(tree, tree_params, cv=5, n_jobs=1, verbose=True)
    locally_best_tree.fit(X_train, y_train)
    print('Best params GridSearchCV: {}'.format(locally_best_tree.best_params_))
    print('Best cross validation score GridSearchCV: {}'.format(locally_best_tree.best_score_))
    tuned_tree = DecisionTreeClassifier(random_state=17, max_depth=9)
    tuned_tree.fit(X_train, y_train)
    tuned_tree_predictions = tuned_tree.predict(X_test)
    print('Accuracy tuned tree: {}'.format(accuracy_score(y_test, tuned_tree_predictions)))
    # plt.show()


def last_end():
    print('\nThe End')


if __name__ == '__main__':
    init_first()
    # test_adult()
    # calculate_entropy()
    analise_adult_dadaframe()
    last_end()
