# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab3b_Act2.py
# Date: 11 September 2020
import math

#observer coordinates
x0= int(input("Enter the x position of the observer: "))
y0= int(input("Enter the y position of the observer: "))
z0= int(input("Enter the z position of the observer: "))

#point 1
x1= int(input("Enter the x position of point 1: "))
y1= int(input("Enter the y position of point 1: "))
z1= int(input("Enter the z position of point 1: "))

#point 2
x2= int(input("Enter the x position of point 2: "))
y2= int(input("Enter the y position of point 2: "))
z2= int(input("Enter the z position of point 2: "))

print("\nObserver location is x=",x0,"y=",y0,"z=",z0)
print(" Point 1 location is x=",x1,"y=",y1,"z=",z1)
print(" Point 2 location is x=",x2,"y=",y2,"z=",z2)

#vector 1
v1x= x1-x0
v1y= y1-y0
v1z= z1-z0
#magnitude
v1m= math.sqrt(v1x**2+v1y**2+v1z**2)

#vector 2
v2x= x2-x0
v2y= y2-y0
v2z= z2-z0
#magnitude
v2m= math.sqrt(v2x**2+v2y**2+v2z**2)

#dot product
dp= v1x*v2x + v1y*v2y + v1z*v2z

#angle between vectors
angle= (math.acos(dp/(v1m*v2m)))*180/math.pi

print("\nThe angle between the points is %.3f"%angle, "degrees")