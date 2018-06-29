#dynamic programming : policy vs value iteration for a 4x4 gridworld
import numpy as np
import sys
import matplotlib.pyplot as plt

def policy_iteration(policy, theta, gamma):
	#initialise the value function with zeroes
	v = np.zeros(16)
	probs = np.zeros((16,16))
	#declare a policy with all 4 directions equally possible
	for i in range(16):
		if i%4 != 0: probs[i][i - 1] = 0.5
		if i%4 != 3: probs[i][i + 1] = 0.5
		if i > 3: probs[i - 4][i] = 0.5
		if i < 12: probs[i + 4][i] = 0.5
	probs[0][1] = 0
	probs[0][4] = 0 #sink

	while True:
		print policy

		delta = 0
		#policy evaluation
		while delta < theta:
			print "lo"
			for i in range(1,16):
				temp = v[i]
				v[i] = 0
				for j in range(16):
					v[i] = v[i] + probs[j][i]*(-1 + gamma*v[j])
				delta = max(delta, max(temp - v[i], v[i] - temp))

		for i in range(4):
			print v[i:i + 4]

		#policy improvement
		stable = True
		for s in range(1,16):
			temp = int(policy[s])
			maxval = -1e9
			for j in range(16):
				if probs[j][s] != 0:
					maxval = probs[j][s]*(-1 + gamma*v[j])
					policy[s] = j
					break

			for j in range(16):
				if probs[j][s]*(-1 + gamma*v[j]) > maxval:
					maxval = probs[j][s]*(-1 + gamma*v[j])
					policy[s] = j

			if policy[s] != temp:
				stable = False

		if stable == True:
			break

policy = np.zeros(16)

policy_iteration(policy, 100, 0.99)

print policy
