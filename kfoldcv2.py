import main as data
import numpy as np
import linreg
import cs373linearsvm as model
import matplotlib.pyplot as plt

model_opt = input("CHOOSE THE MODEL (0: LinearSVC && 1: RadialSVC):")
k_opt = input("CHOOSE THE VALUE OF K for CROSS VALIDATION: ")
acc_arr = []
mis_arr = []
acc_v_arr = []
mis_v_arr = []
size_X = []
size_y = []
k_arr = []

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
        X_train.append(list(X_train_2[i]))
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

def main(fold, model_opt, k):
    t_d, pred = data.main()
    X = t_d[:, 1:len(t_d[0])]
    y = t_d[:, 0]
    X_train, Validation, y_train, y_validation = run(fold, k, X, y)
    '''
    print "Total Length: ", len(X)
    print "Length of training set: ", len(X_train)
    print "Length of Validation Set: ", len(Validation)
    print "Length of labels for training: ", len(y_train)
    print "Length of labels for validation: ",  len(y_validation)
    '''
    acc, mis, acc_valid, mis_valid = model.main(model_opt, X_train, Validation, y_train, y_validation)
    print acc
    acc_arr.append(acc)
    print acc_arr
    mis_arr.append(mis)
    size_X.append(len(X_train))
    size_y.append(len(y_train))
    acc_v_arr.append(acc_valid)
    mis_v_arr.append(mis_valid)
    k_arr.append(k)

for i in range(0, int(k_opt) + 1):
    for j in range(1, i):
        main(j, int(model_opt), i)

plt.ylabel('Number of Correct Classification')
plt.xlabel('Value of K')
plt.scatter(k_arr, acc_arr)
plt.show()
