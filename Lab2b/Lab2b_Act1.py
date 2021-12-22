# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Yida Zou
# Section:      462
# Assignment:   Lab 2b-1
# Date:         5 9 2020
#

import math


resistance=20
current=5
voltage= resistance*current
print("Voltage is", voltage, "V")

mass=100
velocity=21
kinetic_energy= .5*mass*velocity**2
print("Kinetic energy is", kinetic_energy, "J")

days=5
i_amount=3
half_life=3.8
o_amount= i_amount*2**(0-days/half_life)
print("Radon-222 left is", o_amount, "g")

normal_stress=20
angle_of_internal_friction=35*math.pi/180
cohesion=2
shear_stress= normal_stress*math.tan(angle_of_internal_friction)+cohesion
print("Shear stress is", shear_stress, "lbf/in^2")