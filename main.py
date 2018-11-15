import csv
import pandas as pd
import numpy as np

def main():
    data = pd.read_csv("/Users/vishaalbommena/Desktop/year_prediction.csv", sep=',', quotechar='"', header=0)
    data = data[['label', 'TimbreAvg1', 'TimbreAvg2', 'TimbreAvg3', 'TimbreAvg4', 'TimbreAvg5', 'TimbreCovariance1', 'TimbreCovariance2', 'TimbreCovariance3', 'TimbreCovariance4', 'TimbreCovariance5']]
    X = data.as_matrix()
    X = X[:int(0.01*len(X))]
    print X
    print "len(X): ", len(X)

    
main()
