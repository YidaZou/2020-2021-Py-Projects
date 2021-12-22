# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab3a_Act2.py
# Date: 11 September 2020


#takes inputs of names and birthdays from all 4 users
u1_name = input("User 1, please enter your name:")
u1_bday = input("User 1, please enter your birthday in ‘DD MM YYYY’ format:")
u2_name = input("User 2, please enter your name:")
u2_bday = input("User 2, please enter your birthday in ‘DD MM YYYY’ format:")
u3_name = input("User 3, please enter your name:")
u3_bday = input("User 3, please enter your birthday in ‘DD MM YYYY’ format:")
u4_name = input("User 4, please enter your name:")
u4_bday = input("User 4, please enter your birthday in ‘DD MM YYYY’ format:")

#outputs names and birthdays in formatted and aligned columns with labels
print("%20s %11s" % ("Name", "Birthday"))
print("%20s %11s" % (u1_name, u1_bday))
print("%20s %11s" % (u2_name, u2_bday))
print("%20s %11s" % (u3_name, u3_bday))
print("%20s %11s" % (u4_name, u4_bday))
