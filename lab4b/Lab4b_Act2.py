# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab4b_Act2.py
# Date: 19 September 2020

day = int(input("Please enter a positive value for day: "))

if day<0:
    print("You entered an invalid number!")
elif day <=10:
    initial = 10  
    widgets = initial *day
elif 10<day<=60:
    initial = 10
    full = 40
    widgets = initial*10 + full*(day-10)
elif 60<day<100:
    initial = 10
    full = 40
    lessProductionSlope = -1
    lessProduction = 40 + (lessProductionSlope*(day-60))
    widgets = initial*10 + full*(60-10) + (day-60)*((39+lessProduction)/2)
elif day>=100:
    d=99
    initial = 10
    full = 40
    lessProductionSlope = -1
    lessProduction = 40 + (lessProductionSlope*(d-60))
    widgets = initial*10 + full*(60-10) + (d-60)*((39+lessProduction)/2)
    
print("The total number of widgets produced on day",day,"is %.0f"%widgets)