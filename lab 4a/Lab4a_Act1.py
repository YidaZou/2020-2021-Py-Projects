# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Maxine Woods, Katherine Stevens, Michael Tyrrell, Yida Zou
# Section: 462
# Assignment: Lab4a_Act1.py
# Date: 18 09 2020

########## Part A ##########
a= 1 / 7
print (a)
b= a * 7
print (b)
#Yes, the value of b, if we have no roundoff, is 1.

c= 2* a
d= 5* a
e= c + d
print (e)
#No, the value of e is not 1. It’s 0.999999999999

from math import *
x = sqrt (1 / 3)
print (x)
y= x * x * 3
print (y)
z = x * 3 * x
print (z)
#No, y is 1, but z is 0.999999999999

########## Part B ##########
TOL= 1e-10

#check if b and e are equal within specified tolerance
if abs (b-e) < TOL:
    print ("b and e are equal within tolerance of", TOL)
else:
    print ("b and e are NOT equal within tolerance of", TOL)
    
TOL= 1e-10

#check if y and z are equal within specified tolerance
if abs (y-z) < TOL:
    print ("y and z are equal within tolerance of", TOL)
else:
    print ("y and z are NOT equal within tolerance of", TOL)
