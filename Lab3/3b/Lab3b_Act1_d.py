# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab3b_Act1_d.py
# Date: 11 September 2020
import math

print("This program calculates the shear stress given normal stress, cohesion, and angle")
normal_stress=float(input("Please enter the normal stress (lbf/in^2): "))
cohesion=float(input("Please enter the cohesion (lbf/in^2): "))
angle_of_internal_friction=float(input("Please enter the angle (degrees): "))
shear_stress= normal_stress*math.tan(angle_of_internal_friction*math.pi/180)+cohesion
print("Shear stress is %.3f"%shear_stress, "lbf/in^2")