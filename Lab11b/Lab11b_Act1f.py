# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab11b_Act1f.py
# Date: 8 November 2020

def partf(t,d):
    v = []
    for i in range(1,len(t)):
        v.append((d[i]-d[i-1])/(t[i]-t[i-1]))
    return v