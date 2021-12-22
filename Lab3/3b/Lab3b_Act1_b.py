# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab3b_Act1_b.py
# Date: 11 September 2020

print("This program calculates the kinetic energy given mass and velocity")
mass = float(input("Please enter the mass (kg): "))
velocity= float(input("Please enter the velocity (m/s): "))
kinetic_energy= .5*mass*velocity**2
print("Kinetic energy is %.1f"%kinetic_energy, "J")