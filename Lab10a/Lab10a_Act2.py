# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Katherine Stevens, Michael Tyrrell, Yida Zou, Maxine Woods
# Section: 462
# Assignment:  Lab10a_Act2.py
# Date: 31 October 2020

import matplotlib.pyplot as plt
import numpy as np

fig, pb = plt.subplots()
x = np.arange(-2.0, 2.0, 0.01)
y = 1/(4*2)*x**2 #f=2
y1 = 1/(4*6)*x**2 #f=6
pb.plot(x, y, color='r', linewidth=2.0, label = 'f=2')
pb.plot(x, y1, color='b', linewidth=4.0, label = 'f=6')
plt.ylabel('y')
plt.xlabel('x')
plt.suptitle('Parabola Plot with Varying Focal Length')
pb.legend()

# 2 #
fig, poly = plt.subplots()
x = np.linspace(-4.0, 4.0, 25)
y = 2*x**3 + 3*x**2 - 11*x - 6
poly.plot(x,y,'bo')
plt.ylabel('y values')
plt.xlabel('x values')
plt.suptitle('Plot of Cubic Polynomial')


# 3 # 
fig, trig = plt.subplots()
x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = np.sin(x)
y1 = np.cos(x)
trig.plot(x, y, color='r', label = 'cos(x)')
trig.plot(x, y1, color='b', label = 'sin(x)')
plt.ylabel('y values')
plt.xlabel('x values')
plt.suptitle('Plot of cos(x) and sin(x)')
trig.legend()