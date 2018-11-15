import csv
import pandas as pd
import numpy as np
import main as data
import linreg

#/Users/sanatmouli/Desktop/cs373/audio-features-dataset/year_prediction.csv
def main():
#X = np.delete(data.main(), 0, 1)
t_d = data.main()
X = t_d[:, 1:len(t_d[0])]
y = t_d[:, 0]
print (X)
print (y)
B = 30
z = run(B, X, y)
print (z)


def run(B,X,y):
(n, d) = np.shape(X)
z = np.zeros((B, 1))
for i in range(0,B):
u = [0] * n
S = set()
for j in range(0,n):
k = np.random.randint(0,n)
u[j] = k
S.add(k)
T = set(range(0,n)) - S
thetaHat = linreg.run(X[u], y[u])

summ = 0
for t in T:
summ += (y[t] - np.dot(X[t], thetaHat))**2
z[i] = (1.0/len(T))*summ
return z

main()