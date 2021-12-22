# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab10b_Act1.py
# Date: 3 November 2020

import numpy as np
import matplotlib.pyplot as plt


M = np.array([[1.00583, -0.087156], [0.087156, 1.00583]])
v = np.array([[1,0]])
points =np.array([[1,0]])
for i in range(250):
    v = v.dot(M)
    points = np.append(points,v, axis=0)
    
plt.plot(points[:,0],points[:,1])
plt.ylabel('y')
plt.xlabel('x')
plt.suptitle('Spiral')
