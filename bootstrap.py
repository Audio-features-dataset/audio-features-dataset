import csv
import pandas as pd
import numpy as np
import main as data
import random
import linreg
import cs373linearsvm

#/Users/sanatmouli/Desktop/cs373/audio-features-dataset/year_prediction.csv
B = 1


def run (num, X,y):
    n = len(X)
    S = []
    S_y = []
    X_valid = []
    y_valid = []
    indexes = []  
    for i in range(0, num):
        indexes.append(random.randint(0, n))
    for i in range (0, n):
        if i in indexes:
            S.append(list(X[i]))
            S_y.append(y[i])
        else: 
            X_valid.append(list(X[i]))
            y_valid.append(y[i])
    return X_valid, y_valid, S, S_y


def main():
    #X = np.delete(data.main(), 0, 1)
    t_d = data.main()
    X = t_d[:, 1:len(t_d[0])]
    y = t_d[:, 0]
    print X
    print y
    num = 2
    # z = run(B, X, y)
    # print z
    # Xtrain, Xvalid, Ytrain, Yvalid = run(B, X, y)
    X_valid, y_valid, X_train, y_train = run(num , X, y)
    print len(X_valid)
    print X_train
    print y_train

for i in range(0, B):
    print "bth bootstrap: ", i
    main()