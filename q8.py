#Q8. Using relaxation method to solve bvp

import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.inf)
np.set_printoptions(precision = 4)
np.set_printoptions(suppress = True)


xi = 0.
xf = 1.
h = 0.001					#step-size
n = int((xf - xi)/h)

a1 = 0.					#boundary conditions
a2 = 2.					#solving the matrix equation AW + B = C

a = np.zeros(shape = (n-1, n-1))#declaring A matrix
b = np.zeros(shape = (n-1, 1))	#B vector
b[0] = a1						#boundary conditions
b[n-2] = a2
c = np.zeros(shape = (n-1, 1))	#Initialising C vector

for i in range (0, n-1):	#setting A matrix and C vector 
	c[i] = -4*h*h*(xi + i*h) - b[i]
	a[i][i] = -2 - 4*h*h
	if (i-1 == -1): 
		a[i][i+1] = 1
	elif (i == n-2):
		a[i][i-1] = 1
	else: 
		a[i][i+1] = 1
		a[i][i-1] = 1

w = solve(a, c)				#solving for X

x_plot = np.zeros(n+1)
x_plot[n] = 1.
y_plot = np.zeros(n+1)
y_plot[0] = a1
y_plot[n] = a2
y_err = np.zeros(n+1)

y_a = np.zeros(n+1)			
y_a[0] = a1
y_a[n] = a2

for i in range (0, n-1):
	y_plot[i+1] = w[i]			#numerical soln
	x_plot[i+1] = x_plot[i] + h
	y_a[i+1] = np.exp(2)*np.power((np.exp(4) - 1),-1)*(np.exp(2*x_plot[i+1]) - np.exp(-2*x_plot[i+1])) + x_plot[i+1]#analytic soln
	y_err[i+1] = 100*np.absolute(y_a[i+1]-y_plot[i+1])/y_a[i+1]
	
print("The relative perecentage error is:", y_err)			#Relative percentage error

plt.plot(x_plot, y_plot, 'r.', markersize = '3.0', label = 'Numerical solution')
plt.plot(x_plot, y_a, 'g.', markersize = '3.0', label = 'Analytic soln')

plt.title("Q8. Solving bvp using relaxation method")
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()

plt.show()