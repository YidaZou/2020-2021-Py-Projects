# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab11b_Act2.py
# Date: 9 November 2020
import random as rd
def guess():
    return int(input("What is your guess? "))

def compare(z,g):
    if g>z:
        return "Too high!"
    elif g<z:
        return "Too low!"
    
def guessGame():
    print("Guess the secret number! Hint: it’s an integer between 1 and 100...")
    x = int(rd.randint(1, 100))
    n = 0
    g = guess()
    while x!=g:
        print(compare(x,g))
        g = guess()
        n+=1
    return "You guessed it! It took you " + str(n) + " guesses."

print(guessGame())
        

