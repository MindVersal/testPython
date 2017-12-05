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

    # plt.show()


if __name__ == '__main__':
    before_main()
    testing_logres()
    after_main()
