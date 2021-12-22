# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab11b_Act1a.py
# Date: 8 November 2020
t = int(input())
i=1
while i<=t:
    x = input()
    x1 = x.replace('\n','').split(' ')
    n = int(x1[0])
    k = int(x1[1])
    s = int(x1[2])
    
    time = k-1
    time1 = (k-1)+(n+1)
    while k>s:
        k -=1
        time+=1
        print(time)
    while k<=n:
        k+=1
        time+=1
        print(time)
    
    if time< time1:
        time1 = time

    print("Case #"+str(i)+":", time1)
    i+=1
