# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab4b_Act3.py
# Date: 19 September 2020

#user input
a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

#convert to right format
A = ""
if a<0:
    a=0-a
    if a!=1:
        A = "- %i"%a
    else:
        A = "- "
elif a!=1:
    A = "%i"%a
A+="x^2"
if a==0:
    A=""

B = ""    
if b<0:
    b=0-b
    if b!=1:
        B = " - %i"%b
    else:
        B = " - "
elif a!=0:
    if b!=1:
        B = " + %i"%b
    else:
        B = " + "
elif b!=1:
    B = "%i"%b
B+="x"

C = ""
if b==0:
    B=""

if c<0:
    c=0-c
    C = " - %i"%c
else:
    C = " + %i"%c
if c==0:
    C=""
print("The quadratic equation is "+A+B+C+" = 0")