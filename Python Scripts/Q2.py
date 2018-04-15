# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:52:01 2017

@author: Eric Johns
"""
import csv
from random import shuffle
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import re
import time

TRAIN_TO_TEST_RATIO = 0.8
start = time.time()

def shuffle_data(inp, tar):
    combined = list(zip(inp, tar))
    shuffle(combined)
    return zip(*combined)

def from_csv(filename, newline='', delimiter=','):
    x = []
    y = []

    with open(filename, newline=newline) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        
        
        for row in csv_reader:
            x.append(list(map(str, row[1:21]))) #read all input attributes as floats row[:-1]
            y.append(str(row[-1]))

    return x, y

file_name = "datasetchanged1.csv"
x, y = from_csv(file_name)
print(x)
x, y = shuffle_data(x, y) #shuffle data - important as dataset is sorted by class

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = TRAIN_TO_TEST_RATIO) #split dataset into train/test sets
#Default C=0.01, gamma=0.001
C=0.95
gamma=0.0002
clf = svm.SVC(C=C, gamma=gamma, kernel='rbf')
print("C:", C, "gamma:", gamma)

clf.fit(x_train, y_train) #fit to training data

print(classification_report(y_test, clf.predict(x_test)))
end = time.time()
print(end - start, "Seconds")

#for x_i, y_i in zip(x, y):
 #   print("input:", x_i, "target:", y_i)
