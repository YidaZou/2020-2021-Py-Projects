# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Katherine Stevens, Michael Tyrrell, Yida Zou, Maxine Woods
# Section: 462
# Assignment:  Lab12a_Act2.py
# Date: 15 November 2020
import numpy as np

# write a function to calculate sum of areas where height is left side
def calculate1(u, low, up):
    '''Rectangle using the beginning of the interval'''
    ySum = 0
    ySum1 = 0
    d = 10
    x = np.linspace(low, up, d+1)
    w = (up - low) / d
    ySum1 = ySum
    ySum = 0
    for i in range(len(x) - 1):
        if u == 1:
            y = x[i]**3 + 1
        elif u == 2:
            y = 3 * x[i]**3 + 2 * x[i]**2 - 6 * x[i] + 5
        elif u == 3:
            y = 2 * x[i]**3 - x[i]**2 + 3 * x[i] - 2
        ySum += y * w
    tol = 1e-6
    while ySum - ySum1 >= tol or ySum1 - ySum >= tol:
        d += 1
        x = np.linspace(low, up, d+1)
        w = (up - low) / d
        ySum1 = ySum
        ySum = 0
        for i in range(len(x) - 1):
            if u == 1:
                y = x[i]**3 + 1
            elif u == 2:
                y = 3 * x[i]**3 + 2 * x[i]**2 - 6 * x[i] + 5
            elif u == 3:
                y = 2 * x[i]**3 - x[i]**2 + 3 * x[i] - 2
            ySum += y * w
            ySum_ = '%.3f' % ySum
    return ySum_

# write a function to calculate sum of areas where height is right side
def calculate2(u, low, up):
    '''Rectangle using the end of the interval'''
    ySum = 0
    ySum1 = 0
    d = 10
    x = np.linspace(low, up, d+1)
    w = (up - low) / d
    ySum1 = ySum
    ySum = 0
    for i in range(1, len(x)):
        if u == 1:
            y = x[i]**3 + 1
        elif u == 2:
            y = 3 * x[i]**3 + 2 * x[i]**2 - 6 * x[i] + 5
        elif u == 3:
            y = 2 * x[i]**3 - x[i]**2 + 3 * x[i] - 2
        ySum += y * w
    tol = 1e-6
    while ySum - ySum1 >= tol or ySum1 - ySum >= tol:
        d += 1
        x = np.linspace(low, up, d+1)
        w = (up - low) / d
        ySum1 = ySum
        ySum = 0
        for i in range(1, len(x)):
            if u == 1:
                y = x[i]**3 + 1
            elif u == 2:
                y = 3 * x[i]**3 + 2 * x[i]**2 - 6 * x[i] + 5
            elif u == 3:
                y = 2 * x[i]**3 - x[i]**2 + 3 * x[i] - 2
            ySum += y * w
            ySum_ = '%.3f' % ySum
    return ySum_

# write a function to calculate sum of areas where height is the midpoint
def calculate3(u, low, up):
    '''Rectangle using the midpoint of the interval'''
    ySum = 0
    ySum1 = 0
    d = 10
    x = np.linspace(low, up, d+1)
    w = (up - low) / d
    ySum1 = ySum
    ySum = 0
    for i in range(len(x)):
        if u == 1:
            y = x[i]**3 + 1
        elif u == 2:
            y = 3 * x[i]**3 + 2 * x[i]**2 - 6 * x[i] + 5
        elif u == 3:
            y = 2 * x[i]**3 - x[i]**2 + 3 * x[i] - 2
        ySum += y * w
    tol = 1e-6
    while ySum - ySum1 >= tol or ySum1 - ySum >= tol:
        d += 1
        x = np.linspace(low, up, d+1)
        w = (up - low) / d
        ySum1 = ySum
        ySum = 0
        for i in range(len(x)-1):
            if u == 1:
                y = ((x[i]+x[i+1])/2)**3 + 1
            elif u == 2:
                y = 3 * ((x[i]+x[i+1])/2)**3 + 2 * ((x[i]+x[i+1])/2)**2 - 6 * ((x[i]+x[i+1])/2) + 5
            elif u == 3:
                y = 2 * ((x[i]+x[i+1])/2)**3 - ((x[i]+x[i+1])/2)**2 + 3 * ((x[i]+x[i+1])/2) - 2
            ySum += y * w
            ySum_ = '%.3f' % ySum
    return ySum_

# write a function to calculate sum of areas of trapazoids
def calculate4(u, low, up):
    '''Trapezoid'''
    ySum = 0
    ySum1 = 0
    d = 10
    x = np.linspace(low, up, d+1)
    w = (up - low) / d
    ySum1 = ySum
    ySum = 0
    for i in range(len(x)):
        if u == 1:
            y = x[i]**3 + 1
        elif u == 2:
            y = 3 * x[i]**3 + 2 * x[i]**2 - 6 * x[i] + 5
        elif u == 3:
            y = 2 * x[i]**3 - x[i]**2 + 3 * x[i] - 2
        ySum += y * w
    tol = 1e-6
    while ySum - ySum1 >= tol or ySum1 - ySum >= tol:
        d += 1
        x = np.linspace(low, up, d+1)
        w = (up - low) / d
        ySum1 = ySum
        ySum = 0
        for i in range(len(x)-1):
            if u == 1:
                y = x[i + 1]**3 + 1
                y1 = x[i]**3 + 1
            elif u == 2:
                y = 3 * x[i+1]**3 + 2 * x[i+1]**2 - 6 * x[i+1] + 5
                y1 = 3 * x[i]**3 + 2 * x[i]**2 - 6 * x[i] + 5
            elif u == 3:
                y = 2 * x[i+1]**3 - x[i+1]**2 + 3 * x[i+1] - 2
                y1 = 2 * x[i]**3 - x[i]**2 + 3 * x[i] - 2
            ySum += w * (y1 + y) / 2
            ySum_ = '%.3f' % ySum
    return ySum_


print("Which polynomial would you like to test?")
print("1: x^3 + 1")
print("2: 3x^3 + 2x^2 - 6x + 5")
print("3: 2x^3 - x^2 + 3x - 2")
user = float(input("Enter the number: "))
print()
lower = float(input("Enter the lower value for the interval: "))
upper = float(input("Enter the upper value for the interval: "))
print()
# output shape areas
print("Shape 1 area: " + calculate1(user, lower, upper))
print("Shape 2 area: " + calculate2(user, lower, upper))
print("Shape 3 area: " + calculate3(user, lower, upper))
print("Shape 4 area: " + calculate4(user, lower, upper))

