# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab3b_Act1_c.py
# Date: 11 September 2020

print("This program calculates how much Radon-222 is left given time and initial amount")

days=float(input("Please enter the time (days): "))
i_amount=float(input("Please enter the initial amount (g): "))
half_life=3.8
o_amount= i_amount*2**(0-days/half_life)
print("Radon-222 left is %.3f"%o_amount, "g")