# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Katherine Stevens, Michael Tyrrell, Yida Zou, Maxine Woods
# Section: 462
# Assignment:  Lab10a_Act1.py
# Date: 31 October 2020

#“As a team, we have gone through all required sections of the tutorial, and each team member understands the material.”

import numpy as np
rg = np.random.default_rng(1)
A = rg.random((3,4))
B = rg.random((4,2))
C = rg.random((2,3))
D = rg.random((3,1))

E= A @ B @ C
print(E)
print(E.transpose())
print(np.linalg.solve(E, D))


