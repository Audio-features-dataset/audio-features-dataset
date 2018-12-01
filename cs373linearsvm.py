import numpy as np
import main as data
from random import randint
from sklearn import svm
from operator import itemgetter

clf = svm.LinearSVC()
clf1 = svm.SVC(kernel='rbf')

def main(opt, X_train, X_validation, y_train, y_validation):
    print("TRAINING AND PREDICTION PHASE")
    t_d, pred = data.main()
    X = pred[:, 1:len(t_d[0])]
    y = pred[:, 0]
    if opt == 0:
        ml_train(np.array(X_train), np.array(y_train), clf)
    else:
        ml_train(np.array(X_train), np.array(y_train), clf1)
    X_valid = np.array(X_validation)
    y_valid = np.array(y_validation)
    validations = []
    print X_valid
    if opt == 0:
        print "validation"
        validations = ml_predict(np.array(X_valid), clf)
    else:
        print y_valid
        print "validation"
        validations = ml_predict(np.array(X_valid), clf1)
    #print validations

    accuracy = 0
    misclassification = 0
    for i in range(0, len(validations)):
        print "Predicted: ", validations[i]
        print "Actual: ", y_validation[i]
        if validations[i] == y_validation[i]:
            accuracy = accuracy + 1
        else:
            misclassification = misclassification + 1
    print "accuracy: ", accuracy
    print "misclassification: ", misclassification

    predictions = []
    if opt == 0:
        print "prediction"
        predictions = ml_predict(np.array(X), clf)
    else:
        print "prediction"
        predictions = ml_predict(np.array(X), clf1)
    #print predictions
    accuracy = 0
    misclassification = 0
    for i in range(0, len(predictions)):
        if predictions[i] == y[i]:
            accuracy = accuracy + 1
        else:
            misclassification = misclassification + 1
    print "accuracy: ", accuracy
    print "misclassification: ", misclassification

def ml_train(X, y, clf):
    print "Training"
    clf.fit(X, y)

def ml_predict(X_pred, clf):
    predicted = clf.predict(X_pred)
    return predicted

#main(2)
