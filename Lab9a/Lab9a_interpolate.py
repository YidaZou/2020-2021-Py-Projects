# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Katherine Stevens, Michael Tyrrell, Yida Zou, Maxine Woods
# Section: 462
# Assignment:  Lab9a_interpolate.py
# Date: 24 October 2020

file = open("Lab9a_ThermoProperties.csv", "r")

temp = float(input("Enter a temperature between 0 and 260 C: "))
pres = float(input("Enter a pressure between 5 and 10 MPa: "))
print("Properties at "+str(temp)+" C and "+str(pres)+" MPa are:")



line = file.readlines() #rows
#for p=5
for i in range(1,15):
  line[i].replace("\n","")
  l = line[i].split(",") #columns
  for j in range(len(l)):
    l[j] = float(l[j])
  line[i] = l

#for p=10
for i in range(16,30):
  line[i].replace("\n","")
  l = line[i].split(",") #columns
  for j in range(len(l)):
    l[j] = float(l[j])
  line[i] = l

p1=5
p2=10
yValues = []
for x in range(4):
  for i in range(1,14): 
    if line[i][0]<=temp:
      #find t values
      t1=line[i][0]
      t2=line[i+1][0]
      #find y values at p=5
      y1p1=line[i][x+1]
      y2p1=line[i+1][x+1]
      #find y values at p=10
      y1p2=line[i+15][x+1]
      y2p2=line[i+16][x+1]
  yp1 = ((y2p1 - y1p1)/(t2 - t1)) * (temp - t1) + y1p1
  yp2 = ((y2p2 - y1p2)/(t2 - t1)) * (temp - t1) + y1p2
  y = ((yp2 - yp1) / (p2 - p1)) * (pres - p1) + yp1
  yValues.append(y)


print("Specific volume (m^3/kg): %.7f"%yValues[0])
print("Specific internal energy (kJ/kg): %.2f"%yValues[1])
print("Specific enthalpy (kJ/kg): %.2f"%yValues[2])
print("Specific entropy (kJ/kgK): %.4f"%yValues[3])

file.close()




