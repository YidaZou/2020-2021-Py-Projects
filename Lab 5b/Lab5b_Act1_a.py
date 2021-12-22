# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab5b_Act1_a.py
# Date: 26 September 2020

output = ""
#input
n= int(input("Enter a positive integer to compute the Collatz sequence: "))
print("Here is the Collatz sequence starting at "+ str(n)+":")
output+= str(n)
count= 0
while n!=1:
    count+=1
    output+= ", "
    #even
    if n%2==0:
        n= n//2
        output+= str(n)
    #odd
    else:
        n= 3*n+1
        output+= str(n)

print(output)
print("It took",count, "iterations to reach 1")