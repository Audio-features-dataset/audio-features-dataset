import csv
import pandas as pd
import numpy as np
def main():
    data = pd.read_csv("/Users/vishaalbommena/Desktop/year_prediction.csv", sep=',', quotechar='"', header=0)
    data = data[['label', 'TimbreAvg1', 'TimbreAvg2', 'TimbreAvg3', 'TimbreAvg4', 'TimbreAvg5', 'TimbreCovariance1', 'TimbreCovariance2', 'TimbreCovariance3', 'TimbreCovariance4', 'TimbreCovariance5']]
    X = data.as_matrix()
    X = X[:int(0.01*len(X))]
    train = X[:int(0.6*len(X))]
    validation = X[int(0.6*len(X)) + 1: int(0.6*len(X)) + int(0.2*len(X))]
    test = X[int(0.6*len(X)) + int(0.2*len(X)) + 1: int(0.6*len(X)) + int(0.2*len(X)) + int(0.2*len(X))]
    return train, validation, test

main()
