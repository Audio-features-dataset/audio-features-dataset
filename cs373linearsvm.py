import numpy as np
import main as data
from random import randint
from sklearn import svm
from operator import itemgetter

clf = svm.LinearSVC()
clf1 = svm.SVC(kernel='rbf')

def main(opt):
    t_d = data.main()
    X = t_d[:, 1:len(t_d[0])]
    y = t_d[:, 0]
    X_train = X[:int(0.6*len(X))]
    y_train = y[:int(0.6*len(y))]
    if opt == 1:
        ml_train(np.array(X_train), np.array(y_train), clf)
    else:
        ml_train(np.array(X_train), np.array(y_train), clf1)
    X_pred = X[int(0.6*len(X)) + 1:]
    y_pred = y[int(0.6*len(X)) + 1:]
    predictions = []
    if opt == 1:
        predictions = ml_predict(np.array(X_pred), np.array(y_pred), clf)
    else:
        predictions = ml_predict(np.array(X_pred), np.array(y_pred), clf1)
    print predictions
    accuracy = 0
    for i in range(0, len(predictions)):
        if predictions[i] == y_pred[i]:
            accuracy = accuracy + 1
    print accuracy

def ml_train(X, y, clf):
    print "Training"
    clf.fit(X, y)

def ml_predict(X_pred, y_test, clf):
    print "Prediction"
    expected = y_test
    predicted = clf.predict(X_pred)
    return predicted

main(1)
