# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Katherine Stevens, Michael Tyrrell, Yida Zou, Maxine Woods
# Section: 462
# Assignment:  Lab12a_Act1.py
# Date: 14 November 2020

import matplotlib.pyplot as plt
import numpy as np

def toList(c):
  '''Takes input of a string of coefficients and returns a list of the same coefficients.'''
  myList = c.split(' ')
  for i in range(len(myList)):
    myList[i] = float(myList[i])
  return myList

def degree(l):
  '''Takes input of a list of coefficients and returns the highest degreee of the polynomial as an int'''
  dg = len(l)-1
  return dg
  
def makePoints(coF, d):
  '''Takes input of a list of coefficients and the highest degree and returns a list of all the yvalues of the polynomial'''
  xList = np.linspace(-5.0, 5.0, 1000)
  yList = []
  for x in xList:
    y = 0
    for i in range(len(coF)):
      yPart = coF[i]*x**(d-i)
      y += yPart
    yList.append(y)
  return yList

def f(n):
  '''Takes input of a string of coefficients and calculates & returns a list of the yvalues of the polynomial'''
  coF = toList(n)
  d = degree(coF)
  y = makePoints(coF, d)
  return y

def plot(n):
  '''Plots all the curves.'''
  fig, poly = plt.subplots()
  poly.axhline(y=0, color='k')
  poly.axvline(x=0, color='k')
  x = np.linspace(-5.0, 5.0, 1000)
  y = f(n)
  y1 = makePoints(derivative1(),degree(derivative1()))
  y2 = makePoints(derivative2(),degree(derivative2()))
  poly.plot(x,y,'b-.',markersize = 10, label = 'f(x)')
  poly.plot(x,y1,'r:', markersize = 3.2, label = "f'(x)")
  poly.plot(x,y2,'y--', markersize = 6.5, label = "f''(x)")
  yMin = localMin(y)
  y1Min = localMin(y1)
  y2Min = localMin(y2)
  poly.plot(x[yMin[0]],yMin[1],'ko', markersize = 5)
  poly.plot(x[y1Min[0]],y1Min[1],'ko', markersize = 5)
  poly.plot(x[y2Min[0]],y2Min[1],'ko', markersize = 5)
  yMax = localMax(y)
  y1Max = localMax(y1)
  y2Max = localMax(y2)
  poly.plot(x[yMax[0]],yMax[1],'ko', markersize = 5)
  poly.plot(x[y1Max[0]],y1Max[1],'ko', markersize = 5)
  poly.plot(x[y2Max[0]],y2Max[1],'ko', markersize = 5)
  plt.ylabel('y') #label axis
  plt.xlabel('x') #label axis
  plt.suptitle("Plots of f(x), f'(x), f''(x), with local max and min")
  plt.legend()

def derivative1():
  '''Calculates the coefficients of the 1st derivative and outputs them as a list.'''
  coF = toList(userInput)
  dg = degree(coF)
  der1 = []
  for i in range(len(coF)-1):
    coFD = coF[i]*(dg-i)
    der1.append(coFD)
  return der1

def derivative2():
  '''Calculates the coefficients of the 2nd derivative and outputs them as a list.'''
  dg = degree(derivative1())
  der1 = derivative1()
  der2 = []
  for i in range(len(der1)-1):
    coFD2 = der1[i]*(dg-i)
    der2.append(coFD2)
  return der2


def localMax(yList):
  '''Takes input of a list of yvalues and finds the index and y values of the local minimums of each graph and outputs each as seperate lists '''
  maxListX = []
  maxList = []
  for i in range (len(yList)-2):
    if yList[i] < yList[i+1] > yList[i+2]:
      maxList.append(yList[i+1])  
      maxListX.append(i)    
  return [maxListX, maxList] 
  
def localMin(yList):
  '''Takes input of a list of yvalues and finds the index and y values of the local maximums of each graph and outputs each as seperate lists '''
  minListX = []
  minList = []
  for i in range (len(yList)-2):
    if yList[i] > yList[i+1] < yList[i+2]:
      minList.append(yList[i+1])
      minListX.append(i)    
  return [minListX, minList] 



userInput = input('Enter the coefficients, separated by a single space: ')

plot(userInput)



 