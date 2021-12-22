# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Katherine Stevens, Yida Zou, Michael Tyrrell, Maxine Woods
# Section: 462
# Assignment: Lab6a_Act2.py
# Date: 2 October 2020

#variables 
Sex= input("Enter your sex (M/F): ")
Age= int(input("Enter your age (years): "))
Smoker= input("Do you smoke cigarettes (Y/N)? ")
Cholest_total= int(input("Enter your total cholesterol (mg/dL): "))
Cholest_HDL= int(input("Enter your HDL cholesterol (mg/dL): "))
BP= int(input("Enter your systolic BP (mmHg): "))
Meds= input("Are you taking blood pressure medication (Y/N)? ")
Tot_points= 0
Risk = ""

if Sex=="m":
	#age
    if 20<=Age<=34:
        Tot_points -= 9
    elif 35<=Age<=39:
        Tot_points -= 4
    elif 40<=Age<=44:
   		Tot_points += 0
    elif 45<=Age<=49:
   		Tot_points += 3
    elif 50<=Age<=54:
   		Tot_points += 6
    elif 55<=Age<=59:
   		Tot_points += 8
    elif 60<=Age<=64:
   		Tot_points += 10
    elif 65<=Age<=69:
   		Tot_points += 11
    elif 70<=Age<=74:
   		Tot_points += 12
    elif 75<=Age<=79:
        Tot_points += 13
        
	#Cholesterol & Smoker
    if 20 <= Age <= 39:
        if 160 <= Cholest_total <= 199:
            Tot_points += 4
        elif 200 <= Cholest_total <= 239:
            Tot_points += 7
        elif 240 <= Cholest_total <= 279:
            Tot_points += 9
        elif Cholest_total >= 280:
            Tot_points += 11
        if Smoker == "y":
            Tot_points += 8
    if 40 <= Age <= 49:
        if 160 <= Cholest_total <= 199:
            Tot_points += 3
        elif 200 <= Cholest_total <= 239:
        	Tot_points += 5
        elif 240 <= Cholest_total <= 279:
            Tot_points += 6
        elif Cholest_total >= 280:
        	Tot_points += 8
        if Smoker == "y":
        	Tot_points += 5
    if 50 <= Age <= 59:
        if 160 <= Cholest_total <= 199:
        	Tot_points += 2
        elif 200 <= Cholest_total <= 239:
        	Tot_points += 3
        elif 240 <= Cholest_total <= 279:
            Tot_points += 4
        elif Cholest_total >= 280:
        	Tot_points += 5
        if Smoker == "y":
            Tot_points += 3
    if 60 <= Age <= 69:
        if 160 <= Cholest_total <= 199:
        	Tot_points += 1
        elif 200 <= Cholest_total <= 239:
        	Tot_points += 1
        elif 240 <= Cholest_total <= 279:
            Tot_points += 2
        elif Cholest_total >= 280:
        	Tot_points += 3
        if Smoker == "y":
        	Tot_points += 1
    if 70 <= Age <= 79:
        if 160 <= Cholest_total <= 199:
        	Tot_points += 0
        elif 200 <= Cholest_total <= 239:
        	Tot_points += 0
        elif 240 <= Cholest_total <= 279:
            Tot_points += 1
        elif Cholest_total >= 280:
        	Tot_points += 1
        if Smoker == "y":
        	Tot_points += 1

	#HDL
    if Cholest_HDL >=60:
        Tot_points -= 1
    elif 49 >=Cholest_HDL >=40:
        Tot_points += 1
    elif Cholest_HDL < 40:
        Tot_points += 2

	#BP
    if Meds=="y":
        if 120<=BP<=129:
            Tot_points += 1
        elif 130 <=BP<= 139:
            Tot_points += 2
        elif 140 <=BP<= 159:
            Tot_points += 2
        elif BP>=160:
            Tot_points += 3
    else:
        if 130 <=BP<= 139:
            Tot_points += 1
        elif 140 <=BP<= 159:
            Tot_points += 1
        elif BP>=160:
            Tot_points += 2

	#risk
    if Tot_points <0:
        Risk = "<1"
    elif Tot_points <=4:
        Risk = "1"
    elif Tot_points <=6:
   		Risk = "2"
    elif Tot_points <=7:
   		Risk = "3"
    elif Tot_points <=8:
   		Risk = "4"
    elif Tot_points <=9:
   		Risk = "5"
    elif Tot_points <=10:
   		Risk = "6"
    elif Tot_points <=11:
   		Risk = "8"
    elif Tot_points <=12:
   		Risk = "10"
    elif Tot_points <=13:
   		Risk = "12"
    elif Tot_points <=14:
   		Risk = "16"	
    elif Tot_points <=15:
        Risk = "20"	
    elif Tot_points <=16:
   		Risk = "25"
    elif Tot_points >=17:
   		Risk = ">30"


#if patient is female
elif Sex=="f":
	#age
    if 20<=Age<=34:
        Tot_points -= 7
    elif 35<=Age<=39:
        Tot_points -= 3
    elif 40<=Age<=44:
        Tot_points += 0
    elif 45<=Age<=49:
        Tot_points += 3
    elif 50<=Age<=54:
        Tot_points += 6
    elif 55<=Age<=59:
        Tot_points += 8
    elif 60<=Age<=64:
        Tot_points += 10
    elif 65<=Age<=69:
        Tot_points += 12
    elif 70<=Age<=74:
        Tot_points += 14
    elif 75<=Age<=79:
        Tot_points += 16

	#Cholesterol & Smoker
    if 20 <= Age <= 39:
        if 160 <= Cholest_total <= 199:
        	Tot_points += 4
        elif 200 <= Cholest_total <= 239:
        	Tot_points += 8
        elif 240 <= Cholest_total <= 279:
            Tot_points += 11
        elif Cholest_total >= 280:
        	Tot_points += 13
        if Smoker == "y":
            Tot_points += 9
    if 40 <= Age <= 49:
        if 160 <= Cholest_total <= 199:
        	Tot_points += 3
        elif 200 <= Cholest_total <= 239:
        	Tot_points += 6
        elif 240 <= Cholest_total <= 279:
            Tot_points += 8
        elif Cholest_total >= 280:
        	Tot_points += 10
        if Smoker == "y":
        	Tot_points += 7
    if 50 <= Age <= 59:
        if 160 <= Cholest_total <= 199:
        	Tot_points += 2
        elif 200 <= Cholest_total <= 239:
        	Tot_points += 4
        elif 240 <= Cholest_total <= 279:
            Tot_points += 5
        elif Cholest_total >= 280:
        	Tot_points += 7
        if Smoker == "y":
        	Tot_points += 4
    if 60 <= Age <= 69:
        if 160 <= Cholest_total <= 199:
        	Tot_points += 1
        elif 200 <= Cholest_total <= 239:
        	Tot_points += 2
        elif 240 <= Cholest_total <= 279:
            Tot_points += 3
        elif Cholest_total >= 280:
        	Tot_points += 4
        if Smoker == "y":
        	Tot_points += 2 
    if 70 <= Age <= 79:
        if 160 <= Cholest_total <= 199:
        	Tot_points += 1
        elif 200 <= Cholest_total <= 239:
        	Tot_points += 1
        elif 240 <= Cholest_total <= 279:
            Tot_points += 2
        elif Cholest_total >= 280:
        	Tot_points += 2
        if Smoker == "y":
        	Tot_points += 1

	#HDL
    if Cholest_HDL >=60:
        Tot_points -= 1
    elif 49 >=Cholest_HDL >=40:
        Tot_points += 1
    elif Cholest_HDL < 40:
        Tot_points += 2
	
#BP
    if Meds=="y":
        if 120<=BP<=129:
            Tot_points += 3
        elif 130 <=BP<= 139:
            Tot_points += 4
        elif 140 <=BP<= 159:
            Tot_points += 5
        elif BP>=160:
            Tot_points += 6
    else:
        if 120 <= BP <= 129:
            Tot_points += 1
        elif 130 <=BP<= 139:
            Tot_points += 2
        elif 140 <=BP<= 159:
            Tot_points += 3
        elif BP>=160:
            Tot_points += 4
#point to risk
    if Tot_points <9:
        Risk = "<1"
    elif Tot_points <=9:
        Risk = "1"
    elif Tot_points <=10:
        Risk = "1"
    elif Tot_points <=11:
        Risk = "1"
    elif Tot_points <=12:
        Risk = "1"
    elif Tot_points <=13:
        Risk = "2"
    elif Tot_points <=14:
        Risk = "2"
    elif Tot_points <=15:
        Risk = "3"
    elif Tot_points <=16:
        Risk = "4"
    elif Tot_points <=17:
        Risk = "5"
    elif Tot_points <=18:
        Risk = "6"
    elif Tot_points <=19:
        Risk = "8"
    elif Tot_points <=20:
        Risk = "11"
    elif Tot_points <=21:
        Risk = "14"
    elif Tot_points <=22:
        Risk = "17"
    elif Tot_points <=23:
        Risk = "22"
    elif Tot_points <=24:
        Risk = "27"
    elif Tot_points >=25:
        Risk = ">30"

print("Your 10-year risk of a heart attack is " + Risk + "%")
