# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Katherine Stevens, Michael Tyrrell, Yida Zou, Maxine Woods
# Section: 462
# Assignment:  Lab9a_read.py
# Date: 21 October 2020



fileName = input("Enter the filename: ") #read file 
file = open(fileName, "r")
print("5 MPa Data")
print("Temp [C]  v [m3/kg]  u [kJ/kg]  h [kJ/kg]  s [kJ/kgK]")
data = list(file)
line = file.readlines() #split lines into rows
#for p=5
for i in range(1,15):
  line[i].replace("\n","")
  l = line[i].split(",") #split each row
  for j in range(len(l)):
    l[j] = float(l[j])
  print("%8.1f  %8.7f  %9.2f  %9.2f  %10.4f" %(l[0], l[1], l[2], l[3], l[4]))

print()

print("10 MPa Data")
print("Temp [C]  v [m3/kg]  u [kJ/kg]  h [kJ/kg]  s [kJ/kgK]")
#for p=10
for i in range(16,30):
  line[i].replace("\n","")
  l = line[i].split(",") #split each row
  for j in range(len(l)):
    l[j] = float(l[j])
  print("%8.1f  %8.7f  %9.2f  %9.2f  %10.4f" %(l[0], l[1], l[2], l[3], l[4]))

file.close() #close the file


