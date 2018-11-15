import numpy as np
import main as data
from random import randint
from sklearn import svm
from operator import itemgetter
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='scale', kernel='linear',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

clf = svm.SVC()

def main():
    t_d = data.main()
    X = t_d[:, 1:len(t_d[0])]
    y = t_d[:, 0]

    X_train = X[:0.6*len(X)]
    y_train = X[:0.6*len(y)]

    ml_train(np.array(X_train), np.array(y_train), clf)

    X_pred = X[0.6*len(X) + 1:]
    y_pred = y[0.6*len(X) + 1:]

    predictions = ml_predict(np.array(X_pred), np.array(y_pred), clf)
    print predictions
    #accuracy = (X_pred - X_train)/len(y)

def ml_train(X, y, clf):
    clf.fit(np.array(X).reshape(-1, 1), np.array(y))
    
def ml_predict(X_pred, y_test, clf):
    expected = y_test
    predicted = clf.predict(X_pred)
    return predicted

main()
