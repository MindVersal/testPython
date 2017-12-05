import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.model_selection import GridSearchCV


def before_main():
    print('Testing Chapter 04.')


def after_main():
    print('\nThe End.')


def testing_logres():
    print('Testing')
    data = pd.read_csv('../data/microchip_tests.txt', header=None, names=('test1', 'test2', 'released'))
    print(data.info())
    print(data.head())
    X = data.ix[:, :2].values
    y = data.ix[:, 2].values
    plt.scatter(X[y == 1, 0], X[y == 1, 1], c='green', label='Ready')
    plt.scatter(X[y == 0, 0], X[y == 0, 1], c='red', label='Missing')
    plt.xlabel('Test 1')
    plt.ylabel('Test 2')
    plt.title('2 tests microchips')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    before_main()
    testing_logres()
    after_main()
