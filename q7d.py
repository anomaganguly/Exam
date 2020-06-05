 #A linear congruential generator

import numpy as np
from scipy.stats import uniform
import time
import matplotlib.pyplot as plt

a0 = 954								#choice of parameters
c0 = 73
m0 =  201								#range of random number from 0 to 200
x0 = 10.

a1 = 9537113							#choice of parameters
c1 = 713583
m1 =  201								#range of random number from 0 to 200
x1 = 4857.

n = 201									#reqd range
rand0 = np.zeros(n)	
rand0[0] = x0
rand1 = np.zeros(n)						#array to store random number
rand1[0] = x1

for i in range (0, n-1):
	rand0[i+1] = (a0*rand0[i] + c0)%m0
	rand1[i+1] = (a1*rand1[i] + c1)%m1		#generating random number

rand0_new = np.delete(rand0, 0)				#deleting first element i.e. seed value
rand1_new = np.delete(rand1, 0)

if(np.any(rand0_new == x0)):				#checking repetition
	print("seed repeats for first choice")
	
if(np.any(rand1_new == x1)):
	print("seed repeats for second choice")

