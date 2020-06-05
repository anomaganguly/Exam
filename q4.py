#Q4. Random numbers and power spectrum

import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)

n_pts = 1024
nbin = 5
data = np.random.rand(n_pts)

fig1 = plt.figure()
plt.title('Q4. Random numbers uniformly generated between 0 and 1')
plt.plot(data, 'ro', markersize='3')
plt.savefig("q4a.png")

dx = 1										 #spacing
x_min = 0
x = np.arange(n_pts)
ps = np.zeros(n_pts)						 #declaring array for storing the power spectrum values

dft = np.fft.fft(data, norm = 'ortho')		 #numpy discrete fourier transform
k = 2*np.pi*(np.fft.fftfreq(n_pts, d = dx))	 #k values 

factor = np.exp(-1j*k*x_min)
adft = dx*np.sqrt(n_pts/(2*np.pi))*factor*dft #dft according to our convention


for i in range (0, n_pts):
	ps[i] = (1/n_pts)*adft[i]*np.conjugate(adft[i]) #power spectrum

print("Power spectrum values:\n", ps)

fig2 = plt.figure()
plt.plot(k, ps, '-o', markersize = 3)
plt.title('Q4. Power spectrum')
plt.savefig("q4b.png")

kmax = max(k)
kmin = min(k)
print("Minimum value of k is:\n", kmin)
print("\nMaximum value of k is:\n", kmax)

ps_bin = np.zeros(nbin)
k_bin = np.zeros(nbin)

dbin = (kmax - kmin)/(nbin) 

for i in range (nbin):							#averaging over k bins
	p_avg = 0.
	count = 0
	for j in range(n_pts):
		if( k[j] >= kmin + i*dbin and k[j] <= kmin + (i+1)*dbin):
			p_avg = p_avg + ps[j]
			count = count + 1
	ps_bin[i] = p_avg/count
	k_bin[i] = kmin + i*dbin
	
fig3=plt.figure()

plt.bar(k_bin, ps_bin, dbin, align='edge',edgecolor='k')

plt.xlabel('k bins')			#plotting  binned power spectrum
plt.ylabel('P(k)')
plt.title('Q4. Binned Power spectrum')
plt.savefig("q4c.png")
plt.show()

