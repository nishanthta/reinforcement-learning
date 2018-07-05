#Solution to the frozen lake problem involving a 4x4 gridworld using gym
import gym
import numpy as np

env = gym.make('FrozenLake-v0')
#evaluate state value function for a given policy
def eval_policy(env, policy, gamma = 1, theta = 1e-8): #parameters taken from the tutorial
	v = np.zeros(env.nS)

	while True:
		delta = 0 #diff value to check for convergence
		for s in range(env.nS):
			



