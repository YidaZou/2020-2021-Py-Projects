import math
print("This shows the evaluation of sin(x)/x evaluated close to x=0")
print("My guess is 0")
x = 1
while x>= 10**-7:
    print(math.sin(x)/x)
    x/=10
    
print()
print("my guess was close")
