# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab11b_Act1d.py
# Date: 8 November 2020
def partd(f):
    file = open(f, 'r')
    n = file.read()
    n = n.replace(',', '\t')
    f = f.replace('csv','tsv')
    new = open(f, 'w')
    new.write(n)
    file.close()
    new.close()
    return 'Done!'

        