import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV, SGDClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold, GridSearchCV, validation_curve, learning_curve
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.ensemble import RandomForestClassifier


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


def analize_imdb_reviews():
    reviews_train = load_files('../data/aclImdb/train/')
    text_train, y_train = reviews_train.data, reviews_train.target
    # print('Number of documents in training data: {}'.format(len(text_train)))
    # print('Bincounts: {}'.format(np.bincount(y_train)))
    reviews_test = load_files('../data/aclImdb/test/')
    text_test, y_test = reviews_test.data, reviews_test.target
    cv = CountVectorizer()
    cv.fit(text_train)
    print(len(cv.vocabulary_))
    # print(cv.get_feature_names()[50000:50050])
    X_train = cv.transform(text_train)
    X_test = cv.transform(text_test)
    logit = LogisticRegression(n_jobs=-1, random_state=17)
    logit.fit(X_train, y_train)
    print('Score train: {}, \nScore test : {}'.format(round(logit.score(X_train, y_train), 3),
                                                      round(logit.score(X_test, y_test), 3)))
    # visualize_coefficients(logit, cv.get_feature_names())
    text_pipe_logit = make_pipeline(CountVectorizer(),
                                    LogisticRegression(n_jobs=-1, random_state=17))
    text_pipe_logit.fit(text_train, y_train)
    print('Score with pipeline LogisticRegression on test: {}'.format(text_pipe_logit.score(text_test, y_test)))
    param_grid_logit = {'logisticregression__C': np.logspace(-5, 0, 6)}
    grid_logit = GridSearchCV(text_pipe_logit, param_grid_logit, cv=3, n_jobs=-1)
    grid_logit.fit(text_train, y_train)

    print('From grid_logit: \nbest params: {} \nbest score: {}'.format(grid_logit.best_params_,
                                                                       grid_logit.best_score_))
    plot_grid_score(grid_logit, 'logisticregression__C')
    print('Score with grid LogisticRegression on test: {}'.format(grid_logit.score(text_test, y_test)))
    forest = RandomForestClassifier(n_estimators=200, n_jobs=-1, random_state=17)
    forest.fit(X_train, y_train)
    print('Score ForestRandomClassifier: {}'.format(round(forest.score(X_test, y_test)), 3))
    plt.show()


def visualize_coefficients(classifier, feature_names, n_top_features=25):
    coef = classifier.coef_.ravel()
    positive_coefficients = np.argsort(coef)[-n_top_features:]
    negative_coefficients = np.argsort(coef)[:n_top_features]
    interesting_coefficients = np.hstack([negative_coefficients, positive_coefficients])
    plt.figure(figsize=(15, 5))
    colors = ['red' if c < 0 else 'blue' for c in coef[interesting_coefficients]]
    plt.bar(np.arange(2 * n_top_features), coef[interesting_coefficients], color=colors)
    feature_names = np.array(feature_names)
    plt.xticks(np.arange(1, 1 + 2 * n_top_features), feature_names[interesting_coefficients], rotation=60, ha='right')


def plot_grid_score(grid, param_name):
    plt.plot(grid.param_grid[param_name], grid.cv_results_['mean_train_score'], color='green', label='train')
    plt.plot(grid.param_grid[param_name], grid.cv_results_['mean_test_score'], color='red', label='test')
    plt.legend()


def test_xor_problem():
    rng = np.random.RandomState(0)
    X = rng.randn(200, 2)
    y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
    plt.scatter(X[:, 0], X[:, 1], s=30, c=y, cmap=plt.cm.Paired)
    plot_boundary(LogisticRegression(), X, y, 'Logistic Regression, XOR problem')
    logit_pipe = Pipeline([('poly', PolynomialFeatures(degree=2)),
                           ('logit', LogisticRegression())])
    plt.show()
    plot_boundary(logit_pipe, X, y, 'Logistic Regression + quadratic features. XOR problem')
    plt.show()


def plot_boundary(clf, X, y, plot_title):
    xx, yy = np.meshgrid(np.linspace(-3, 3, 50), np.linspace(-3, 3, 50))
    clf.fit(X, y)
    Z = clf.predict_proba(np.vstack((xx.ravel(), yy.ravel())).T)[:, 1]
    Z = Z.reshape(xx.shape)
    image = plt.imshow(Z, interpolation='nearest',
                       extent=(xx.min(), xx.max(), yy.min(), yy.max()),
                       aspect='auto', origin='lover', cmap=plt.cm.PuOr_r)
    contours = plt.contour(xx, yy, Z, levels=[0], linewidths=2, linetypes='--')
    plt.scatter(X[:, 0], X[:, 1], s=30, c=y, cmap=plt.cm.Paired)
    plt.xticks(())
    plt.yticks(())
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.axis([-3, 3, -3, 3])
    plt.colorbar(image)
    plt.title(plot_title, fontsize=12)


def test_telecom_data():
    data = pd.read_csv('../data/telecom_churn.csv').drop('State', axis=1)
    data['International plan'] = data['International plan'].map({'Yes': 1, 'No': 0})
    data['Voice mail plan'] = data['Voice mail plan'].map({'Yes': 1, 'No': 0})
    y = data['Churn'].astype('int').values
    X = data.drop('Churn', axis=1).values
    alphas = np.logspace(-2, 0, 20)
    sgd_logit = SGDClassifier(loss='log', n_jobs=-1, random_state=17)
    logit_pipe = Pipeline([('scaler', StandardScaler()),
                           ('poly', PolynomialFeatures(degree=2)),
                           ('sgd_logit', sgd_logit)])
    val_train, val_test = validation_curve(logit_pipe, X, y, 'sgd_logit__alpha', alphas, cv=5, scoring='roc_auc')
    plot_with_err(alphas, val_train, label='training scores')
    plot_with_err(alphas, val_test, label='validation scores')
    plt.xlabel('Alpha')
    plt.ylabel('ROC AUC')
    plt.legend()
    plt.show()
    plot_learning_curve(degree=2, alpha=10, X=X, y=y)
    plt.show()
    plot_learning_curve(degree=2, alpha=0.05, X=X, y=y)
    plt.show()
    plot_learning_curve(degree=2, alpha=1e-4, X=X, y=y)
    plt.show()


def plot_with_err(x, data, **kwargs):
    mu, std = data.mean(1), data.std(1)
    lines = plt.plot(x, mu, '-', **kwargs)
    plt.fill_between(x, mu - std, mu + std, edgecolor='none', facecolor=lines[0].get_color(), alpha=0.2)


def plot_learning_curve(degree=2, alpha=0.01, X=None, y=None):
    train_sizes = np.linspace(0.05, 1, 20)
    logit_pipe = Pipeline([('scaler', StandardScaler()),
                           ('poly', PolynomialFeatures(degree=degree)),
                           ('sgd_logit', SGDClassifier(n_jobs=-1, random_state=17, alpha=alpha))])
    N_train, val_train, val_test = learning_curve(logit_pipe, X, y, train_sizes=train_sizes, cv=5, scoring='roc_auc')
    plot_with_err(N_train, val_train, label='training scores')
    plot_with_err(N_train, val_test, label='validation score')
    plt.xlabel('Training Set Size')
    plt.ylabel('AUC')
    plt.legend()


if __name__ == '__main__':
    before_main()
    # testing_logres()
    # analize_imdb_reviews()
    # test_xor_problem()
    test_telecom_data()
    after_main()
