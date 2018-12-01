import main as data
import numpy as np
import linreg
import cs373linearsvm as model

def run(fold, k,X,y):
    X_train = []
    y_train = []
    S = []
    y_validation = []
    num_indexes = []
    y_validation = y[fold*k : fold*k + k]
    S = X[fold*k : fold*k + k]

    X_train_1 = X[:fold*k]
    X_train_2 = X[fold*k + k:]
    X_train = list(X_train_1)
    for i in range(0, len(X_train_2)):
        X_train.append(X_train_2[i])

    y_train_1 = y[:fold*k]
    y_train_2 = y[fold*k + k:]
    y_train = list(y_train_1)
    for i in range(0, len(X_train_2)):
        y_train.append(y_train_2[i])
    return X_train, S, y_train, y_validation

def sum(y, X, theta, T):
    sum = 0
    for t in T:
        sum += (y[t] - np.dot(X[t], theta)) ** 2
    return sum

def main(fold):
    print "ENTERED KFOLD"
    t_d, pred = data.main()
    X = t_d[:, 1:len(t_d[0])]
    y = t_d[:, 0]
    X_train, Validation, y_train, y_validation = run(fold, 5, X, y)
    '''
    print "Total Length: ", len(X)
    print "Length of training set: ", len(X_train)
    print "Length of Validation Set: ", len(Validation)
    print "Length of labels for training: ", len(y_train)
    print "Length of labels for validation: ",  len(y_validation)
    '''
    model.main(1, X_train, Validation, y_train, y_validation)

#for i in range(1, 6):
print "ith Set: ", 2
main(2)
