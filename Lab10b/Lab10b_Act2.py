# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab10b_Act2.py
# Date: 3 November 2020

import matplotlib.pyplot as plt

file = open("WeatherData.csv", "r")
line = file.readline().strip('\n').split(',')
dates = []
avgT = []
avgP = []
precip = []
avgD = []
months = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}
monthsH = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}
monthsL = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}
for line in file:
    line = line.strip('\n').split(',')
    dates.append(line[0])
    avgT.append(float(line[2]))
    avgP.append(float(line[11]))
    if float(line[13]) >0:
        precip.append(float(line[13]))
    avgD.append(float(line[5]))
    date = line[0].split('/')
    months[int(date[0])].append(int(line[2]))
    monthsH[int(date[0])].append(int(line[1]))
    monthsL[int(date[0])].append(int(line[3]))
    
# 1 #
fig, avg = plt.subplots()
avg2 = avg.twinx()
avg.plot(dates,avgT, label='T avg')
avg2.plot(dates,avgP,color='r', label = 'P avg')
avg.set_title('Average Temperature and Pressure for Data Range')
avg.set_xlabel('date')
avg.set_ylabel('Average Temperature, F')
avg2.set_ylabel('Average Pressure, inHg')
avg.set_xticks([0,200,400,600,800,1000])
fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=avg.transAxes)

# 2 #
fig, p = plt.subplots()
p.hist(precip, bins = [0,1,2,3,4,5,6,7,8])
p.set_xlabel('Precipitation, in')
p.set_ylabel('Number of days')
p.set_title('Histogram of Precipitation')

# 3 #
fig, d = plt.subplots()
d.scatter(avgT, avgD, s=5)
d.set_xlabel('Average Temperature, F')
d.set_ylabel('Average Dew Point, F')
d.set_title('Dew Point vs Temperature')

# 4 #
for m in range(1,13):
    #avg
    tot=0
    for i in months[m]:
        tot+=float(i)
    avg=tot/len(months[m])
    months[m] = avg
    #high
    monthsH[m] = max(monthsH[m])
    #low
    monthsL[m] = min(monthsL[m])
fig, t = plt.subplots()
t.bar(range(len(months)), list(months.values()), color = 'gray')
t.plot(range(len(months)), list(monthsH.values()), color='r', label = 'High T')
t.plot(range(len(months)), list(monthsL.values()), color='b', label = 'Low T')
t.set_xlabel('Month')
t.set_ylabel('Average Temperature, F')
t.set_title('Average Temperature by Month')
t.legend()