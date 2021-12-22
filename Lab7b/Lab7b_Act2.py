# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab7b_Act2.py
# Date: 11 October 2020
from math import *

inA = input("Enter the elements for vector A: ")
inB = input("Enter the elements for vector B: ")
A = inA.split()
B = inB.split()
l = len(A) #dimension of vector
for i in range(l):
    A[i] = float(A[i])
    B[i] = float(B[i])

#magnitude
totA = 0
totB = 0
for i in range(l):
    totA+= A[i]**2
    totB+= B[i]**2
magA= sqrt(totA)
magB= sqrt(totB)
print("The magnitude of vector A is %.5f" %magA)
print("The magnitude of vector B is %.5f" %magB)

#A+B
ApB= []
for i in range(l):
    ApB.append(A[i]+B[i])
print("A + B is", ApB)
#A-B
AmB= []
for i in range(l):
    AmB.append(A[i]-B[i])
print("A - B is", AmB)
#dot product
dot= 0
for i in range(l):
    dot+= A[i]*B[i]
print("The dot product is", dot)
