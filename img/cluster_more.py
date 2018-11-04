import matplotlib.pyplot as plt
import json
import numpy as np
import pdb

# K means algorithm

def getGroups(mids, data, k):
	groups = [[] for i in range(0,k)]
	for d in data:
		groups[getMid(d, mids, k)].append(d)
	return groups

def getNewMids(groups, k, n):
	avgs = []
	for i in range(0, k):
		if len(groups[i]) > 0:
			avgs.append(np.average(groups[i], 0))
		else:
			avgs.append(np.random.rand(n))
	return np.array(avgs)

def getMid(pt, mids, k):
	dists = [np.linalg.norm(pt-mids[i]) for i in range(0,k)]
	minIdx = 0
	for i in range(1, k):
		if dists[i] < dists[minIdx]:
			minIdx = i
	return minIdx


def getFit(data, k, n):
	mids = np.random.rand(k, n)
	ITTERS = 500
	for i in range(ITTERS):
		groups = getGroups(mids, data, k)
		mids = getNewMids(groups, k, n)
	return mids


def nBestFits(i, arr, n, taboo):
	# STUPID 
	dists = []

	for j in range(len(arr)):
		if j != i and j not in taboo:
			dists.append((np.linalg.norm(arr[i]-arr[j]), j))
	dists.sort(key=lambda x: x[0])
	return dists[:n]

def dSum(ds):
	s = 0
	for d in ds:
		s +=d[0]
	return s

if __name__ == "__main__":
	with open('data.json', 'r') as f:
		data = json.load(f)
	x = np.array(data).reshape(6*3*3,3)/255
	itpts = getFit(x, 6, 3)

	taboo = []
	reses = []
	for start in range(9*6):
		res = nBestFits(start, x, 9, taboo)
		reses.append((dSum(res), res))
	reses.sort(key=lambda x: x[0])
	good = reses[0][1]
	g1Inds = [goodi[1] for goodi in good]
	taboo += g1Inds
	group1 = [goodi[0] for goodi in good]

	g1Colors = np.array([x[ti] for ti in g1Inds])

	plt.imshow(g1Colors.reshape(1,*g1Colors.shape))
	plt.show()

	import pdb; pdb.set_trace()

	# groups = getGroups(itpts, x, 6)

	# for g in groups:
	# 	plt.imshow(groups.reshape(1,*g.shape))
	# 	plt.show()

	# plt.imshow(x.reshape(1,*x.shape))
	# plt.show()
	print(itpts)
	plt.imshow(itpts.reshape(1,*itpts.shape))
	plt.show()
