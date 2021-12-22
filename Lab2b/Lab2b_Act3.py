# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Yida Zou
# Section:      462
# Assignment:   Lab 2b-3
# Date:         5 9 2020
#

x = 1
z = 0
z += x
print(z)

y = 10
x += 1 #x=2
y *= x #y=20
y += x
x = 1
y += x #y=23
z += y
print(z)

y = 10
z = 0
z += y
z += y
z += x
x = y
y *= x
z += y
z += y
z += y
print(z)

x = y
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
z = 0
z += y
print(z)

z = 0
y = 10
z += y
z += y
z += y
y *= x
z += y
z += x
z += x
x = 1
x += 1
z += x
z += x
print(z)








