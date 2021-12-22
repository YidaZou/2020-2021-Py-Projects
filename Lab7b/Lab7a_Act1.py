# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Maxine Woods, Katherine Stevens, Michael Tyrrell, Yida Zou
# Section: 462
# Assignment: Lab7a_Act1.py
# Date: 10 October 2020

#PART A#

prices = input("Enter three or more stock prices separated by spaces: ")
priceList = prices.split()

#convert list to float
for i in range(len(priceList)):
  priceList[i] = float(priceList[i])
#print each with decimal lined up 
for i in range(len(priceList)):
  priceList[i] = "%.2f" %priceList[i]
for i in range(len(priceList)):  
  print("$" + priceList[i].rjust(7))


#myString = ‘The value of myVar is %6.2f’ % myVar
#print(myString)
#PART B#
print()

separator = input("Enter a two-character separator: ")
priceList = prices.split()


#print each with decimal lined up 
print(priceList[0], end=" ")
for i in range(1,len(priceList)):
  print(separator + " " + str(priceList[i]), end=" ")
