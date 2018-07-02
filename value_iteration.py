#dynamic programming : policy vs value iteration for a 4x4 gridworld
from __future__ import print_function
import numpy as np
import sys
import matplotlib.pyplot as plt
from prob import neighbours, probs

def value_iteration(iterations, gamma):

	vold = np.zeros(16)
	vnew = np.zeros(16)

	for cnt in range(iterations):
		vold = vnew[:]
		delta = 0

		for s in range(1,16):
			vprobs = [probs[j][s]*(-1 + gamma*vold[s]) for j in neighbours[s]]
			vnew[s] = max(vprobs)

	for i in range(4):
		print(vnew[i*4:i*4 + 4])

	#define policy
	policy = np.zeros(16)
	for s in range(1,16):
		temp = int(policy[s])
		maxval = -1e9
		#used to C++, forgive the piece of code below
		cnt, idx = 0, -1
		for k in neighbours[s]:
			if vnew[k] > maxval:
				maxval = vnew[k]
				#print(s, " ", k)
				idx = k
			cnt = cnt + 1
		policy[s] = idx

	print(policy)


value_iteration(100, 0.99)