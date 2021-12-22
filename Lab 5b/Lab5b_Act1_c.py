# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Yida Zou
# Section: 462
# Assignment: Lab5b_Act1_c.py
# Date: 27 September 2020

primes=0
for n in range(101):
    if n>=2:
        for i in range(2,n):
            if n%i==0:
                print(str(n)+" is not prime")
                break
        else:
            print(str(n)+" is prime")
            primes+=1

print("There are "+str(primes)+" prime numbers between 2 and 100")