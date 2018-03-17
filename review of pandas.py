# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 11:21:28 2018

@author: Webster
"""
# This code simply works loads in data from a remote file. 
#the figures are not factual.

import pandas as pd
import numpy
import csv
x = []
for line in open(r"C:\Users\Webster\Documents\planets.csv"):
    x = line.split(",")
    for row in x:
        print(x) 
#converting the above data into an array
X = numpy.array(x)
print (X)
# we may also read the data using pandas using the following method
x = pd.read_csv(r"C:\Users\Webster\Documents\planets.csv")
print (x)
#we can eliminate the headers in the dataset using the header=None method
x = pd.read_csv(r"C:\Users\Webster\Documents\planets.csv", header = None)
print (x)
#more concerning dataframes
airline = pd.read_csv(r"C:\Users\Webster\Documents\passdata.csv", header = None)
print(airline)
print(airline.columns)
airline.columns=["year", "passengers"]
print(airline.columns)
print(airline["passengers"])
airline["ones"] = 1
print(airline)
#joining data
d1 = pd.read_csv(r"C:\Users\Webster\Documents\data1.csv", header = None)
print (d1)
d2 = pd.read_csv(r"C:\Users\Webster\Documents\data2.csv", header = None)
print (d2)


