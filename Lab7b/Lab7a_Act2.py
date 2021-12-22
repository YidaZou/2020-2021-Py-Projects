# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Maxine Woods, Katherine Stevens, Michael Tyrrell, Yida Zou
# Section: 462
# Assignment: Lab7a_Act2.py
# Date: 10 October 2020


# Grade Data for Lab7 Activity 2

gradeData=[69,99,73,59,67,65,52,99,57,58,67,88,72,69,41,74,53,90,63,66,92,54,61,59,48,71,83,89,100,69,66,39,48,41,99,68,52,78,77,73,40,65,77,87,96,44,54,60,89,72]

#Part A
sum = 0
for i in range (len(gradeData)):
  sum += gradeData[i]
avg = sum / len(gradeData)
print("The mean is %.2f" %avg)


#Part B
from math import *
var = 0
for i in range(len(gradeData)):
  var += (gradeData[i] - avg) ** 2
stanDev = sqrt((1/len(gradeData)*var))

print("The standard deviation is %.4f" %stanDev)

#Part C
min = gradeData[0]
for i in range(len(gradeData)): 
  if gradeData[i] < min: 
    min = gradeData[i]
print("The min is", min)

#max

max = gradeData [0]
for i in range (len(gradeData)):
    if gradeData[i] > max:
      max = gradeData [i]
print("The max is", max)
  