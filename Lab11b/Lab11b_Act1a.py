# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab11b_Act1a.py
# Date: 8 November 2020

import numpy as np

def parta(l,w,h,r):
    rV = l*w*h
    if r<=l/2:
        cV = np.pi*r**2*h
        return rV-cV
    else:
        t = 2*np.arccos(1-(r-l/2)/r)
        aS = 4*((r**2/2)*(t-np.sin(t)))
        aC = (np.pi*r**2)-aS
        cV = aC*h
        if rV-cV<=0.01:
            return 0
        else:
            return rV-cV
