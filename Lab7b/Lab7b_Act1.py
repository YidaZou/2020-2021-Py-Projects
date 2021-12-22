# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab7b_Act1.py
# Date: 11 October 2020

name = input("What is your name? ")
v = True #if name begins with vowel sound
vowels = ['A','E','I','O','U']
for i in range(len(vowels)):
    if name[0] == vowels[i]:
        out = name.lower()
        v = False
twoL = ['Ch', 'Sc', 'Tr']

if v:
    out = name[1:]
    for i in range(len(twoL)):
        if name[0:2] == twoL[i]:
            out = name[2:]
print(name +", " +name +", " + "Bo-B"+out)
print("Banana-Fana Fo-F"+out)
print("Me Mi Mo-M"+out)
print(name+"!")