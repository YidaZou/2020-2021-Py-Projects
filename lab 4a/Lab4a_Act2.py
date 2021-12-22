# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Maxine Woods, Katherine Stevens, Michael Tyrrell, Yida Zou
# Section: 462
# Assignment: Lab4a_Act1.py
# Date: 19 09 2020

#prompt user to enter hours parked in decimal form
print("Enter the hours parked as a decimal number. Include a negative sign if the ticket is lost.")
z= float(input("Please enter the hours parked: "))
h= z #original input
y=0 #fee total
#for input of negative sign, we change x to positive value to calculate fee and add penalty fee
if z < 0:
	y+=36
	z = 0 - z
#rounds up decimal to integer
x=(z//1)
if z>x:
	x+=1


#use if/elif statements to assign correct fee
if 0<x<=2:
    y+=4
elif 2<=x<=4:
    y+= 4+3
elif 5<=x<=21:
    y+= 7+(x-4)
elif 22<=x<=24:
    y+=24
elif 24<x:
    a = x//24
    b = x%24
    y+= 24*a
    if 0<b<=2:
        y+=4
    elif 2<=b<=4:
        y+= 7
    elif 5<=b<=21:
        y+= 7+(b-4)
    elif 21<b<24:
        y+=24

print("Parking for",h,"hours please pay $%.0f"%y)
    
