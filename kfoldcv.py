import main as data
import numpy as np
import linreg

def run(k,X,y):
    n = len(X)
    z = np.zeros((k, 1))
    for i in range(k):
        T = set(range(int(np.floor((n * i) / k)), int(np.floor((n * (i + 1) / k) - 1) + 1)))
        S = set(range(n)) - T
        theta = linreg.run(X, y)
        summ = sum(y, X, theta, T)
        z[i] = (1.0/len(T))*(float(summ))
    return z

def sum(y, X, theta, T):
    sum = 0
    for t in T:
        sum += (y[t] - np.dot(X[t], theta)) ** 2
    return sum

def main():
    print "ENTERED KFOLD"
    t_d = data.main()
    X = t_d[:, 1:len(t_d[0])]
    y = t_d[:, 0]
    print (X)
    print (y)
    z = run(5, X, y)
    print z

main()
