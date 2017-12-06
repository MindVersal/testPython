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


def plot_boundary(clf, X, y, grid_step=0.01, poly_featurizer=None):
    x_min, x_max = X[:, 0].min() - .1, X[:, 0].max() + .1
    y_min, y_max = X[:, 1].min() - .1, X[:, 1].max() + .1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, grid_step),
                         np.arange(y_min, y_max, grid_step))
    Z = clf.predict(poly_featurizer.transform(np.c_[xx.ravel(), yy.ravel()]))
    Z = Z.reshape(xx.shape)
    plt.contour(xx, yy, Z, cmap=plt.cm.Paired)


def plot_scatter_X(X, y):
    plt.scatter(X[y == 1, 0], X[y == 1, 1], c='green', label='Ready')
    plt.scatter(X[y == 0, 0], X[y == 0, 1], c='red', label='Missing')
    plt.xlabel('Test 1')
    plt.ylabel('Test 2')
    plt.title('2 test microchips')
    plt.legend()


def testing_logres():
    print('Testing')
    data = pd.read_csv('../data/microchip_tests.txt', header=None, names=('test1', 'test2', 'released'))
    # print(data.info())
    # print(data.head())
    X = data.ix[:, :2].values
    y = data.ix[:, 2].values
    # plt.scatter(X[y == 1, 0], X[y == 1, 1], c='green', label='Ready')
    # plt.scatter(X[y == 0, 0], X[y == 0, 1], c='red', label='Missing')
    # plt.xlabel('Test 1')
    # plt.ylabel('Test 2')
    # plt.title('2 tests microchips')
    # plt.legend()
    # print(X[y == 1, 0])
    # plot_scatter_X(X, y)
    poly = PolynomialFeatures(degree=7)
    X_poly = poly.fit_transform(X)
    # C = 1e-2
    # C = 1e+2
    C = 1e+4
    logit = LogisticRegression(C=C, n_jobs=-1, random_state=17)
    logit.fit(X_poly, y)
    # plot_boundary(logit, X, y, grid_step=.01, poly_featurizer=poly)
    # plot_scatter_X(X, y)
    print('Round Score: {}'.format(round(logit.score(X_poly, y), 3)))
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=17)
    c_values = np.logspace(-2, 3, 500)
    logit_searcher = LogisticRegressionCV(Cs=c_values, cv=skf, verbose=1, n_jobs=-1)
    logit_searcher.fit(X_poly, y)
    print('Score: {}'.format(round(logit_searcher.score(X_poly, y), 3)))
    # Print Validation
    # i_min = 1
    # i_max = 1000
    # i_step = 1
    # i_mult = 0.01
    # plt.scatter([i * i_mult for i in range(i_min, i_max, i_step)],
    #             [LogisticRegression(C=i*i_mult, n_jobs=-1, random_state=17).fit(X_poly, y).score(X_poly, y)
    #              for i in range(i_min, i_max, i_step)], label='C')
    # plt.xlabel('C')
    # plt.ylabel('LogReg')
    # plt.title('Test C')
    # plt.legend()
    # for c in [2, 10, 100, 300, 650, 990]:
    #     logist_reg = LogisticRegression(C=c, n_jobs=-1, random_state=17).fit(X_poly, y)
    #     print('Score LogisticRegression: {}'.format(logist_reg.score(X_poly, y)))

    plt.show()


if __name__ == '__main__':
    before_main()
    testing_logres()
    after_main()
