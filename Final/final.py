#https://tamu.zoom.us/j/96133714694

import sympy as sy
import statistics as stat
import numpy as np
import matplotlib.pyplot as plt
import sys

def end():
  '''Terminates the program'''
  print("Thank you for using our Calculator")
  sys.exit(0)

def Calculator():
  '''This function asks the user for input of an expression to be evaluated by addition, subtraction, multiplication or division between numbers. It will then allow the user to choose between returning to the menu or entering another expression.'''
  try:
    expression = input("Enter an expression for addition, subtraction, multiplication or division (use +, -, *, and /): ")
    value = eval(expression)
    print(value)
  except:
    print('Please enter a valid expression')
    Calculator()
  next = input("Enter 'E' to end or 'R' to return to menu or press Enter to input another expression: ")
  try:
    if next == 'R' or next == 'r':
      Menu()
    elif next == 'E' or next == 'e':
      end()
  except SyntaxError:
    print('Please enter a valid expression')
    Calculator()
  Calculator()



def CalcFileMenu():
  '''This function prints the calculator file menu. This allows the user to choose which operation they would like to do with a file.'''
  print("Please enter your choice(1-4) or")
  print("Enter 'E' to end or 'R' to return to menu:")
  print(" 1 - Output Sum")
  print(" 2 - Output Average")
  print(" 2 - Output Standard Deviation")
  print(" 4 - Output all of the above")
  choice = input()
  return choice
  


def CalcFile():
  '''This function allows the user to call in a file for the calculator to read and uses the CalcFileMenu function to let them choose what they want to do with the data in that file.'''
  print("Make sure your file has no text and is only a list of numbers,")
  print("Please enter the .csv file you want to calculate from, including the file extension(.csv)")
  print("Otherwise, Enter 'E' to end or 'R' to return to menu: ")
  fName = input()
  try:
    if fName == 'R' or fName == 'r':
      Menu()
    elif fName == 'E' or fName == 'e':
      end()
    else:
      file=open(fName,'r')
  except (SyntaxError, FileNotFoundError) as a:
    print("Not a valid input")
    CalcFile()
  numbers=file.read().replace('\n','').split(',')
  numbers=list(map(int,numbers))
  s = sum(numbers)
  a = stat.mean(numbers)
  sD = stat.stdev(numbers)
  try:
    choice = CalcFileMenu()
    if int(choice) == 1:
      print("Sum:",s)
    elif int(choice) == 2:
      print("Average:",a)
    elif int(choice) == 3:
      print("Standard Deviation:",sD)
    elif int(choice) == 4:
      print("Sum:",s)
      print("Average:",a)
      print("Standard Deviation:",sD)
    elif choice == 'R' or choice == 'r':
      file.close()
      Menu()
    elif choice == 'E' or choice == 'e':
      file.close()
      end()
    else:
      print("Not a choice")
      CalcFile()
  except SyntaxError:
    print("Not a choice")
    CalcFile()
  next = input("Enter 'E' to end or 'R' to return to menu or press Enter to input another file: ")
  try:
    if next == 'R' or next == 'r':
      Menu()
    elif next == 'E' or next == 'e':
      end()
  except SyntaxError:
    print('Please enter a valid expression')
    CalcFile()
  CalcFile()
  
  
def Graph():
  '''
  This function allows the user to graph a polynomial 
  '''
  x,y=sy.symbols('x,y')
  try:
    print("Please enter the coefficients of your polynomial seperated by a single space: ")
    print("The program will automatically assign degrees to the polynomials")
    print("Ex: '3 -2 4' would be '3x^2-2x+4'")
    print("Your graph will appear once you end the program.")
    print("Otherwise, Enter 'E' to end or 'R' to return to menu: ")
    function=input()
    if function == 'R' or function == 'r':
      Menu()
    elif function == 'E' or function == 'e':
      end()
    else:
      plot(function)
  except:
    print('Please enter a valid expression')
    Graph()
    next = input("Enter 'E' to end or 'R' to return to menu: ")
  next = input("Enter 'E' to end or 'R' to return to menu: ")
  try:
    if next == 'R' or next == 'r':
      Menu()
    elif next == 'E' or next == 'e':
      end()
  except SyntaxError:
    print('Please enter a valid expression')
    Graph()

  
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
  poly.plot(x,y,'b-.',markersize = 10, label = 'f(x)')

  plt.ylabel('y') #label axis
  plt.xlabel('x') #label axis
  plt.suptitle("Plot of f(x)")
  plt.legend()



def Menu():
  '''This function allows the user to choose what they'll like the calculator to perform.'''

  print("Please enter a choice(1-4)")
  print(" 1 - Calculator")
  print(" 2 - Calculate From File")
  print(" 3 - Graph a Function")
  print(" 4 - End Program")
  try:
    choice = input()
    if int(choice) == 1:
      Calculator()
    elif int(choice) == 2:
      CalcFile()
    elif int(choice) == 3:
      Graph()
    elif int(choice) == 4:
      end()
    else:
      print("Not a choice")
      Menu()
  except (SyntaxError,ValueError) as b:
    print("Not a choice")
    Menu()

Menu()