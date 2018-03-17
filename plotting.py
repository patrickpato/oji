# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 12:29:57 2018

@author: Webster
"""

import numpy
import pandas as pd
import matplotlib.pyplot as plt
#matplotlib is used to visualize the data that is obtained from loading datasets using pandas and numpy. it makes use of various graphical features such as sine waves, cosine waves, quadratci functions, etc. 
# data signl can be considered to be a sine wave. lets therefore plot a wave for a wifi signal strength between o and 100 seconds using  1second step. 
x = numpy.linspace(0, 100, 100)
y = numpy.sin(x)
plt.plot(x, y)
print(plt.show)
#the plot shows how the signal may vary in strength over time/

#additional features such as labels and titles can be added to the plot as shown below. 
plt.xlabel("time")
plt.ylabel("signalstrength")
plt.title("signal time curve")
print(plt.show)

