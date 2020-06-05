#Q10. Fourier transform of box function using NumPy

import numpy as np
import matplotlib.pyplot as plt

def fn(x):													#defining the function
	if(np.absolute(x) <= 1.):
		return 1.
	else:
		return 0.


n_pts = 1024												#number of points

x_min = np.array([[-4.], [-50.] , [-150.]])					#range of x (3 samplings)
x_max = np.array([[4.], [50.], [150.]])
dx = (x_max-x_min)/(n_pts - 1)								#sampling rate

x = np.zeros(shape=(3, n_pts))								#declaring the arrays
fx = np.zeros(shape=(3, n_pts))
fk = np.zeros(shape=(3, n_pts))
k = np.zeros(shape=(3, n_pts))
fk_plot = np.zeros(shape=(3, n_pts)) 
fk_a = np.zeros(shape=(3, n_pts)) 

for i in range (0, 3):
	for j in range (0, n_pts):
		fx[i][j] = fn(x_min[i] + j*dx[i])					#setting the values of fn in array
		x[i][j] = x_min[i] + j*dx[i]
	fk[i,:] = np.fft.fft(fx[i,:], norm='ortho')				#numpy fourier transform
	k[i,:] = 2*np.pi*(np.fft.fftfreq(n_pts, d = dx[i]))		#k values 
	factor = np.exp(-1j*k[i,:]*x_min[i])
	fk_plot[i,:] = dx[i]*np.sqrt(n_pts/(2*np.pi))*factor*fk[i,:]	#fourier transform according to our convention
	
	
fig1, axes = plt.subplots(figsize=(13, 5), nrows = 1, ncols = 2)	#plotting fx and fk for different samplings

axes[0].plot(x[0,:], fx[0,:], '-o', linewidth = 0.5, markersize = 3, label = "Box function")
axes[0].set_xlim([-5.0, 5.0])											
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].set_title('Box function')

axes[1].plot(k[0,:], fk_plot[0,:], '-o', linewidth = 0.5, markersize = 3, label = "Fourier transform")
axes[1].set_xlim([-50.0 ,50.0])
axes[1].set_xlabel('k')
axes[1].set_ylabel('f(k)')
axes[1].set_title('Fourier transform')

fig1.tight_layout()

fig2, axes = plt.subplots(figsize=(13, 5), nrows = 1, ncols = 2)	#plotting

axes[0].plot(x[1,:], fx[1,:], '-o', linewidth = 0.5, markersize = 3, label = "Box function")
axes[0].set_xlim([-5.0, 5.0])											
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].set_title('Box function')

axes[1].plot(k[1,:], fk_plot[1,:], '-o', linewidth = 0.5, markersize = 3, label = "Fourier transform")
axes[1].set_xlim([-50.0 ,50.0])
axes[1].set_xlabel('k')
axes[1].set_ylabel('f(k)')
axes[1].set_title('Fourier transform')

fig2.tight_layout()

fig3, axes = plt.subplots(figsize=(13, 5), nrows = 1, ncols = 2)	#plotting

axes[0].plot(x[2,:], fx[2,:], '-o', linewidth = 0.5, markersize = 3, label = "Box function")
axes[0].set_xlim([-5.0, 5.0])											
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].set_title('Box function')

axes[1].plot(k[2,:], fk_plot[2,:], '-o', linewidth = 0.5, markersize = 3, label = "Fourier transform")
axes[1].set_xlim([-50.0 ,50.0])
axes[1].set_xlabel('k')
axes[1].set_ylabel('f(k)')
axes[1].set_title('Fourier transform')

fig3.tight_layout()

plt.show()