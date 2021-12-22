# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab6b_Act2.py
# Date: 5 October 2020
strain = float(input("Enter the strain: "))
if 0<=strain<=0.01:
    stress=(44/0.01)*strain
    print("The stress is approximately %.1f" %stress)
elif 0.01<strain<=0.06:
    stress=44
    print("The stress is approximately %.1f" %stress)
elif 0.06<strain<=0.18:
    stress=((60-44)/(0.18-0.06))*(strain-0.06)+44
    print("The stress is approximately %.1f" %stress)
elif 0.18<strain<=0.26:
    stress=((50-60)/(0.26-0.18))*(strain-0.18)+60
    print("The stress is approximately %.1f" %stress)
else:
    print("Strain is undefined in that region")