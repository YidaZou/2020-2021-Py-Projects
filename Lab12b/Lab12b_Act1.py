# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab12b_Act1.py
# Date: 15 November 2020
import turtle as t

def toNum(n):
    """Takes input of one integer and converts it to a string of roman numerals
        Input: Integer
        Return: String"""
    #list of digits
    dig = [1000, 900, 500, 400,
           100, 90, 50, 40,
           10, 9, 5, 4, 1]
    #list of Roman numerals
    num = ["M", "CM", "D", "CD",
           "C", "XC", "L", "XL",
           "X", "IX", "V", "IV", "I"]
    out = ''
    x = 0
    #loop through all digits of n
    while  n> 0:
        #convert digit to corresponding numeral
        for i in range(n // dig[x]):
            out += num[x]
            n -= dig[x]
        x += 1
    return out

def toImage(num):
    """Takes input of one string of Roman numerals and draws the Roman numerals using turtle
        Input: String"""
    t.write(num)
    t.done()

uI = int(input("Enter an integer: "))   #user input

toImage(toNum(uI))  #turtle drawing after conversion