#dynamic programming : policy vs value iteration for a 4x4 gridworld
import numpy as np
import sys
import matplotlib.pyplot as plt

def policy_iteration(policy, theta, gamma):
	#initialise the value function with zeroes
	vold = np.zeros(16)
	vnew = np.zeros(16)
	probs = np.zeros((16,16))
	#declare probabilities by hardcoding (looping is longer lol)
	probs[2][3], probs[7][3], probs[14][15], probs[11][15], probs[13][12], probs[8][12] = 0.5, 0.5, 0.5, 0.5, 0.5, 0.5
	probs[0][1], probs[2][1], probs[5][1], probs[1][2], probs[3][2], probs[6][2] = 0.33, 0.33, 0.33, 0.33, 0.33, 0.33
	probs[3][7], probs[6][7], probs[11][7], probs[7][11], probs[10][11], probs[15][11] = 0.33, 0.33, 0.33, 0.33, 0.33, 0.33
	probs[12][13], probs[9][13], probs[14][13], probs[13][14], probs[10][14], probs[15][14] = 0.33, 0.33, 0.33, 0.33, 0.33, 0.33
	probs[0][4], probs[5][4], probs[8][4], probs[4][8], probs[9][8], probs[12][8] = 0.33, 0.33, 0.33, 0.33, 0.33, 0.33
	for i in range(1,16):
		if np.count_nonzero(probs[i]) == 0:
			probs[i][i - 1], probs[i][i + 1], probs[i - 4][i], probs[i + 4][i] = 0.25, 0.25, 0.25, 0.25


	while True:
		vold = vnew[:]
		vnew = np.zeros(16)

		delta = 0
		#policy evaluation
		while delta < theta:
			for i in range(1,16):
				temp = vold[i]
				for j in range(16):
					vnew[i] = vnew[i] + probs[j][i]*(-1 + gamma*vold[j])
				delta = max(delta, abs(vnew[i] - vold[i]))

		for i in range(4):
			print(vnew[i:i + 4])

		#policy improvement
		stable = True
		for s in range(1,16):
			temp = int(policy[s])
			maxval = -1e9
			for j in range(16):
				if probs[j][s] != 0:
					maxval = probs[j][s]*(-1 + gamma*vnew[j])
					policy[s] = j
					break

			for j in range(16):
				if probs[j][s]*(-1 + gamma*vnew[j]) > maxval:
					maxval = probs[j][s]*(-1 + gamma*vnew[j])
					policy[s] = j

			if policy[s] != temp:
				stable = False

		if stable == True:
			break

policy = np.zeros(16)

policy_iteration(policy, 0.1, 1)

print(policy)
