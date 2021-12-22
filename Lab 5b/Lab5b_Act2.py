# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab5b_Act2.py
# Date: 27 September 2020

#input
n= int(input("Please enter an integer: "))
print("The first "+str(n)+" estimates of the Golden ratio are:")
F0=1
F1=1
output= "1.000"
i=1
while i<n:
    F2 = F1+F0
    e = F2/F1 #estimate
    output+= ", "+"%.3f"%e
    F0 = F1
    F1 = F2
    i+=1
    
print(output)

