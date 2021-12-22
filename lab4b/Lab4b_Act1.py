# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab4b_Act1.py
# Date: 19 September 2020

n1= float(input("Enter number 1: "))
n2= float(input("Enter number 2: "))
n3= float(input("Enter number 3: "))

if n1>=n2 and n1>=n3:
    print("The largest number is",n1)
elif n2>=n1 and n2>=n3:
    print("The largest number is",n2)
else:
    print("The largest number is",n3)