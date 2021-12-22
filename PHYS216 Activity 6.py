"""
Activity 6

Yida Zou
"""
import numpy as np
from math import*
import matplotlib.pyplot as plt
#assumptions 
g=9.81 #m/s
h=10 #meters
mb=70 #kg
vb=5 #m/s
rhoAluminum=2700 #kg/m^3

omega1=1.5
#Mass of the drum
M=((2*g*h/vb**2)-1)*2*mb
print("M_drum= %6.2f kg"%M)

#1 Inertia as a function of omega

omega=np.linspace(2,5,20)

I=(mb/omega**2)*(2*g*h-vb**2)
plt.figure(1)
plt.plot(omega,I)
plt.xlabel('omega(rad/s)')
plt.ylabel('I(kgm^2)')

#2 Radius as a function of omega

R=vb/omega

plt.figure(2)
plt.plot(omega,R)
plt.xlabel('omega(rad/s)')
plt.ylabel('R(m)')

#2 Depth as a function of the radius

d=M/(pi*R**2*rhoAluminum)

plt.figure(3)
plt.plot(R,d*1000)
plt.xlabel('R(m)')
plt.ylabel('depth(mm)')

#recommended values for drum
omega1 = 3 #selected value of omega
I1=(mb/omega1**2)*(2*g*h-vb**2) #moment
R1=vb/omega1 #radius
d1=d=M/(pi*R1**2*rhoAluminum) #depth
print("Omega_drum= %6.2f rad/s"%(omega1))
print("I_drum= %6.2f Kgm^2"%(I1))
print("R_drum= %6.2f m"%(R1))
print("d_drum= %6.2f mm"%(d1*1000))