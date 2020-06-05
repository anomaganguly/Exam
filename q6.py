#Q6. Solving coupled ivp

import numpy as np
import math
import matplotlib.pyplot as plt

def f(y1, y2, x):
	f1 = 32*y1 + 66*y2 + (2./3.)*x + (2./3.)
	f2 = -66*y1 - 133*y2 - (1./3.)*x - (1./3.)
	return (np.asarray([f1, f2]))

a = 0						#range of x is from (a, b)
b = 0.5
h = 0.001					#step-size
n = np.int((b - a)/h)		#number of points

y1 = np.empty(n+1)			#initialising arrays for solution
y2 = np.empty(n+1)
x = np.empty(n+1)

y1[0] = 1./3.				#setting the initial conditions
y2[0] = 1./3.


for i in range (0, n):		#RK4
	x[i+1] = x[i] + h
	k1 = h*f(y1[i], y2[i], x[i])[0]
	l1 = h*f(y1[i], y2[i], x[i])[1]
	
	k2 = h*f(y1[i] + k1/2., y2[i] + l1/2., x[i] + h/2.)[0]
	l2 = h*f(y1[i] + k1/2., y2[i] + l1/2., x[i] + h/2.)[1]
	
	k3 = h*f(y1[i] + k2/2., y2[i] + l2/2., x[i] + h/2.)[0]
	l3 = h*f(y1[i] + k2/2., y2[i] + l2/2., x[i] + h/2.)[1]
	
	k4 = h*f(y1[i] + k3, y2[i] + l3, x[i] + h)[0]
	l4 = h*f(y1[i] + k3, y2[i] + l3, x[i] + h)[1]
	
	y1[i+1] = y1[i] + 1/6*(k1 + 2*(k2 + k3) + k4)
	
	y2[i+1] = y2[i] + 1/6*(l1 + 2*(l2 + l3) + l4)
	
fig = plt.figure()	
plt.plot(x, y1, 'r.', markersize='3.0', label='y1')	#plotting
plt.plot(x, y2, 'b.', markersize='3.0', label='y2')

plt.xlabel('x')
plt.ylabel('y1(x), y2(x)')
plt.title("Q6. Solving couples ivp using RK4")
plt.legend()
plt.show()