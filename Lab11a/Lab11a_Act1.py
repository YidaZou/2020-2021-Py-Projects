# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Katherine Stevens, Michael Tyrrell, Yida Zou, Maxine Woods
# Section: 462
# Assignment:  Lab11a_Act1.py
# Date: 7 November 2020

import numpy as np


x = float(input("Enter an initial guess for a root of f(x): "))

#Test Functions:
#F = x**2 - 1
#F = x**2 - 3x - 4
#F = x**2 + 2x + 1
#F = x**2 + 2x - 1
#F = x**2 - 2x - 1

def F(x): # create function for F
  F = 7*x**3 - 3*x**2 + 12*x - 50
  return F
def deriv(x): # derivative function using .001 as a
  a = 0.001
  d = (F(x+a)-F(x))/a 
  return d
def newton_step(xi): #Newton's method
  xNext =  xi - F(xi) / deriv(xi)
  return xNext
def newton(x0): #function for list of approximations
  tol = 1e-6 #tolerance
  rtList=[]
  rt1 = x0
  rt2 = newton_step(rt1)
  rtList.append(rt1)
  rtList.append(rt2)
  while rt1 - rt2 > tol or rt2 - rt1 > tol:
    rt1 = rt2
    rt2 = newton_step(rt1)
    rtList.append(rt2)
  return rtList

print("The root approximations are:") #print approximations
root = newton(x)
print("%.6f"%root[0], end = '')
i=1
while i<len(root): #use while loop to print in format
  print(" -> %.6f" %root[i], end = '')
  i+=1

