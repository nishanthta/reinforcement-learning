#dynamic programming : policy vs value iteration for a 4x4 gridworld
from __future__ import print_function
import numpy as np
import sys
import matplotlib.pyplot as plt
from prob import neighbours, probs

def policy_iteration(policy, iterations, gamma):
	#initialise the value function with zeroes
	vold = np.zeros(16)
	vnew = np.zeros(16)

	while True:
		#print(policy)
		delta = 0
		#policy evaluation
		for cnt in range(iterations):
			vold = vnew[:]
			vnew = np.zeros(16)

			for i in range(1,16):
				temp = vold[i]
				for j in range(16):
					vnew[i] = vnew[i] + probs[j][i]*(-1 + gamma*vold[j])
				delta = max(delta, abs(vnew[i] - vold[i]))

		for i in range(4):
			print(vnew[i*4:i*4 + 4])
		print("\n")	

		#policy improvement
		stable = True
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


			if policy[s] != temp:
				stable = False

		if stable == True:
			break

policy = np.zeros(16)

policy_iteration(policy, 10, 0.99)

print(policy)