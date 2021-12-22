# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Maxine Woods, Katherine Stevens, Michael Tyrrell, Yida Zou
# Section: 462
# Assignment: Lab4a_Act1.py
# Date: 19 09 2020

########## Part A ##########
a = input("Enter True or False for a: ")
if a == 'T' or a =='t' or a =='True':
    a = True
elif a == 'F' or a =='f' or a =="False":
    a = False

b = input("Enter True or False for b: ")
if b == 'T' or b =='t' or b =='True':
    b = True
elif b == 'F' or b =='f' or b =="False":
    b = False

c = input("Enter True or False for c: ")
if c == 'T' or c =='t' or c =='True':
    c = True
elif c == 'F' or c =='f' or c =="False":
    c = False

########## Part B ##########
print (a and b and c)
print (a or b or c)

########## Part C ##########
print((a or b) and not(a and b) and not(not a and not b))
print((a and b and c) or (not b and not c and a) or (not c and not a and b) or (not a and not b and c))