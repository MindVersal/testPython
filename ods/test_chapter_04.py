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
    print(data.info())
    print(data.head())
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
    plot_boundary(logit, X, y, grid_step=.01, poly_featurizer=poly)
    plot_scatter_X(X, y)
    print('Round Score: {}'.format(round(logit.score(X_poly, y), 3)))
    plt.show()


if __name__ == '__main__':
    before_main()
    testing_logres()
    after_main()
