"""
question 5

Yida Zou
"""
import numpy as np

A=np.array([[1,1],[0.14,1]])
b=np.array([10000,2500])
x=np.linalg.solve(A,b)
print('q2=',x[0])
print('q3=',x[1])