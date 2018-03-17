# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 10:40:52 2018

@author: Webster
"""
# 50 engineers and 30 doctors attended a workshop where they were asked a number of questions. the total number of points answered by the two groups was 75. in a simmilar workshop, 78 engineers and 25 doctors were present. this time the totl points obtained was 35. find x and y where x is the average value of points by engineers and y is the average value by doctors.
#this is a sample solution for the word problem above.
#the number of doctors and engineers in the workshop can be considered to be a 2 by 2 matrix.
#the total number of points is the value used in obtaining the solution. 
#the linalg function is used in the computation as show below. 
import numpy
a = ([50, 30], [78, 25])
A = numpy.array(a)
print (a)
M = numpy.matrix(a)
print(M)
b = ([75, 35])
x_y = numpy.linalg.inv(M).dot(b)
print (x_y)
# from the solution....seems like engineers are dumb. 

#3508 Africans and 2000 Asians were subjected to a Malaria vulnerability test and the total number of positive results obtained was 100. a second experiment was conducted using 5000 Africans and 7200 Asians and the results were 85. find the vuknerability constant for the two groups. 
m = ([3508, 2000], [5000, 7200])
M = numpy.matrix(m)
print(M)
results = (100, 85)
vul_const = numpy.linalg.inv(M).dot(results)
print(vul_const)
#As shown from the above data, Africans are more likely to get Malaria compared  to Asians. the reasons are obvious.
#various other computations can be made on the data above. these include finding their covariance among many more. lets attempt the covariance. 
covr = numpy.cov(M)
print(covr)