# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Bonus_activity.py
# Date: 6 November 2020
file = open("Bonus_activity_grades.txt", "r")
pP = 0 #possible points
#Exam 1
line = file.readline().strip('\n').split(',')
e1= int(line[1])
pP+=15
#Exam 2
line = file.readline().strip('\n').split(',')
e2=0
if line[1]!='':
    e2= int(line[1])
    pP+=20

#Lab assignments
line = file.readline().strip('\n').split(',')
sum = 0
for i in line[1:]:
    sum+=int(i)
lAvg = sum/(len(line)-1)
pP+=30

#Class activities
line = file.readline().strip('\n').split(',')
sum = 0
for i in line[1:]:
    sum+=int(i)
cAvg = sum/(len(line)-1)
pP+=19

#Dept Modules
line = file.readline().strip('\n').split(',')
dM=0
if line[1]!='':
    dM= int(line[1])
    pP+=8

#Industry essay
line = file.readline().strip('\n').split(',')
iE=0
if line[1]!='':
    iE= int(line[1])
    pP+=1.5

#DI Sat essay
line = file.readline().strip('\n').split(',')
dE=0
if line[1]!='':
    dE= int(line[1])
    pP+=1.5

#Project
line = file.readline().strip('\n').split(',')
p=0
if line[1]!='':
    p= int(line[1])
    pP+=5

grade = ((.15*e1 + .20*e2 + .30*lAvg + .19*cAvg + .05*p + .08*dM + .015*iE + .015*dE)/pP)*100
print("My grade so far is %.1f" %grade)
file.close()