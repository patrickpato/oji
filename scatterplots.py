# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:04:51 2018

@author: Webster
"""
import pandas as pd
import numpy
import matplotlib.pyplot as plt
#matplotlib can also be used for scatterplots. 
B = pd.read_csv(r"C:\Users\Webster\Documents\d3.csv", header = None).as_matrix()
x = B[:, 0]
y = B[:, 1]
plt.scatter(x, y)
print(plt.show)
#fitting a line into our scatter plot
x_line = numpy.linspace(0, 1000, 1000)
y_line = 5 * x_line + 1
plt.scatter(x, y)
print(plt.show) 
plt.plot(x_line, y_line)
print(plt.show)

