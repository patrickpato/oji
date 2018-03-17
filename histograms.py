# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:14:35 2018

@author: Webster
"""
#plotting a histogram using the matplotlib
import pandas as pd
import numpy
import matplotlib.pyplot as plt
B = pd.read_csv(r"C:\Users\Webster\Documents\d3.csv", header = None).as_matrix()
x = B[:, 0]
y = B[:, 1]
# plotting a histogram for x values
plt.hist(x)
print(plt.show)
#let us visually show the distribution of random data using a histogram
data = numpy.random.random(1000000)
plt.hist(data)
print(plt.show)