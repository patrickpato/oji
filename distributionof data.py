# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:18:45 2018

@author: Webster
"""
import pandas as pd
import numpy
import matplotlib.pyplot as plt
#let us visually show the distribution of random data using a histogram
data = numpy.random.random(1000000)
plt.hist(data)
print(plt.show)
#the uniformity of the histogram says it all. 
#altering data
y_actual = 2*x + 1
deficit = y - y_actual
plt.hist(deficit)
print(plt.show)
#not soo goood
