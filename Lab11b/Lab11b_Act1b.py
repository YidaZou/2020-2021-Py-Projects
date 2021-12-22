# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab11b_Act1b.py
# Date: 8 November 2020

def partb(n,c,v):
    f = 0
    least = v[0]-c[0]
    for i in range(len(c)):
        if v[i]-c[i]<least:
            f = i
            least = v[i]-c[i]
    return (n[f], least)
