# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab7b_Act3.py
# Date: 11 October 2020

#part A
userIn = input("Enter a list of values: ")
unsorted = userIn.split()
for i in range(len(unsorted)):
    unsorted[i] = float(unsorted[i])
    
sort = []
while len(unsorted)>0:
    sort.append(min(unsorted))
    unsorted.remove(min(unsorted))

#part B
mn = sort[0]
mx = sort[len(sort)-1]
print("The minimum value is", mn)
print("The maximum value is", mx)

if len(sort)%2 == 0:
    med = (sort[len(sort)//2] + sort[len(sort)//2-1])/2
else:
    med = sort[len(sort)//2]
    
print("The median is", med)