# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab5b_Act1_b.py
# Date: 26 September 2020

#input
n= int(input("Enter an integer: "))
x=n #store n for printing
sum=0
product=1
while n>0:
    sum+=n
    product*=n
    n-=1
    
print("The sum of all integers from 0 to "+str(x)+" is "+str(sum))
print("The product of all integers from 1 to "+str(x)+" is "+str(product))