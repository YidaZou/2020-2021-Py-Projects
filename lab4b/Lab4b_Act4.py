# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab4b_Act4.py
# Date: 19 September 2020

from math import *
#user input
a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

#root calculations
if a==0 and b==0 and c!=0:
    print("You entered an invalid combination of coefficients")
elif a==0:
    rt= (0-c)/b
else:
    if b**2-4*a*c >=0:
        rt1= ((0-b)+sqrt(b**2-4*a*c))/(2*a)
        rt2= ((0-b)-sqrt(b**2-4*a*c))/(2*a)
    else:
        rt1= str((0-b)/2) + " + " + str(0-(b**2-4*a*c)/4) +"i"
        rt2= str((0-b)/2) + " - " + str(0-(b**2-4*a*c)/4) +"i"
        
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
   

    
#root formatting
if a==0:
    print("The root of the equation "+A+B+C+" = 0 is x =",rt)
elif a!=0 and b!=0 and c!=0:
    if rt1==rt2:
        print("The root of the equation "+A+B+C+" = 0 is x =",rt1)
    else:
        print("The roots of the equation "+A+B+C+" = 0 are x =",rt1,"and x =",rt2)
    
        