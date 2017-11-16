import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier


def f(x):
    x = x.ravel()
    return np.exp(-x ** 2) + 1.5 * np.exp(-(x - 2) ** 2)


def generate(n_samples, noise):
    X = np.random.rand(n_samples) * 10 - 5
    X = np.sort(X).ravel()
    y = np.exp(-X ** 2) + 1.5 * np.exp(-(X - 2) ** 2) + np.random.normal(0.0, noise, n_samples)
    X = X.reshape((n_samples, 1))
    return X, y


def plotting_predict_of_tree():
    print('Predict DecisionTreeRegressor')
    n_train = 150
    n_test = 1000
    noise = 0.1
    X_train, y_train = generate(n_samples=n_train, noise=noise)
    X_test, y_test = generate(n_samples=n_test, noise=noise)
    reg_tree = DecisionTreeRegressor(max_depth=5, random_state=17)
    reg_tree.fit(X_train, y_train)
    reg_tree_pred = reg_tree.predict(X_test)
    plt.figure(figsize=(10, 6))
    plt.plot(X_test, f(X_test), 'b')
    plt.scatter(X_train, y_train, c='b', s=20)
    plt.plot(X_test, reg_tree_pred, 'g', lw=2)
    plt.xlim([-5, 5])
    plt.title('Decision tree regression, MSE = {}'.format(np.sum((y_test - reg_tree_pred) ** 2)))
    plt.show()


def analise_kneigebors_churn():
    df = pd.read_csv('../data/telecom_churn.csv')
    df['International plan'] = pd.factorize(df['International plan'])[0]
    df['Voice mail plan'] = pd.factorize(df['Voice mail plan'])[0]
    df['Churn'] = df['Churn'].astype('int')
    states = df['State']
    y = df['Churn']
    df.drop(['State', 'Churn'], axis=1, inplace=True)
    X_train, X_holdout, y_train, y_holdout = train_test_split(df.values, y, test_size=0.3, random_state=17)
    tree = DecisionTreeClassifier(max_depth=5, random_state=17)
    knn = KNeighborsClassifier(n_neighbors=10)
    tree.fit(X_train, y_train)
    knn.fit(X_train, y_train)
    tree_pred = tree.predict(X_holdout)
    print('Accuracy Decision Tree Classifier = {}'.format(accuracy_score(y_holdout, tree_pred)))
    knn_pred = knn.predict(X_holdout)
    print('Accuracy K Neighbors Classifier = {}'.format(accuracy_score(y_holdout, knn_pred)))
    print('\nAuto find best params.')
    print(' - Decision Tree Classifier - ')
    tree_params = {'max_depth': range(1, 11),
                   'max_features': range(4, 19)}
    tree_grid = GridSearchCV(tree, tree_params, cv=5, n_jobs=-1, verbose=True)
    tree_grid.fit(X_train, y_train)
    print('Best params : {}'.format(tree_grid.best_params_))
    print('Best score : {}'.format(tree_grid.best_score_))
    print('Accuracy Decision Tree Classifier with auto configuration = {}'
          .format(accuracy_score(y_holdout, tree_grid.predict(X_holdout))))
    print('- K Neighbors Classifier - ')
    knn_pipe = Pipeline([('scaler', StandardScaler()), ('knn', KNeighborsClassifier(n_jobs=-1))])
    knn_params = {'knn__n_neighbors': range(1, 10)}
    knn_grid = GridSearchCV(knn_pipe, knn_params, cv=5, n_jobs=-1, verbose=True)
    knn_grid.fit(X_train, y_train)
    print('Best params : {}'.format(knn_grid.best_params_))
    print('Best score : {}'.format(knn_grid.best_score_))
    print('Accuracy K Neighbors Classifier with auto configuration = {}'
          .format(accuracy_score(y_holdout, knn_grid.predict(X_holdout))))
    print('- Random Forest Classifier - ')
    forest = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=17)
    print('Mean cross validation score = {}'
          .format(np.mean(cross_val_score(forest, X_train, y_train, cv=5))))
    forest_params = {'max_depth': range(1, 11),
                     'max_features': range(4, 19)}
    forest_grid = GridSearchCV(forest, forest_params, cv=5, n_jobs=-1, verbose=True)
    forest_grid.fit(X_train, y_train)
    print('Best params : {}'.format(forest_grid.best_params_))
    print('Best score : {}'.format(forest_grid.best_score_))
    print('Accuracy Random Forest Classifier with auto configuration = {}'
          .format(accuracy_score(y_holdout, forest_grid.predict(X_holdout))))
    # print(df.head())


if __name__ == '__main__':
    print('Testing Chapter 03')
    # plotting_predict_of_tree()
    analise_kneigebors_churn()
