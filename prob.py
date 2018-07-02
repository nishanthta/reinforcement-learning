import numpy as np

neighbours = [[1,4],[0,2,5],[1,3,6],[2,7],[0,5,8],[1,4,6,9],[2,5,7,10],[3,6,11],[4,9,12],[5,8,10,13],[6,9,11,14],[7,10,15],[8,13],[9,12,14],[10,13,15],[11,14]]

probs = np.zeros((16,16))

#couldn't pythonify this next part enough
for i in range(1,16):
	if len(neighbours[i]) == 2:
		for j in neighbours[i]: probs[j][i] = 0.5
	if len(neighbours[i]) == 3:
		for j in neighbours[i]: probs[j][i] = 0.33
	if len(neighbours[i]) == 4:
		for j in neighbours[i]: probs[j][i] = 0.25