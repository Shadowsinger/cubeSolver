
# scramble all colors (assumes there is a small discrete ammount of colors)

from PIL import Image
import numpy as np
import json

colors = []

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
	ITTERS = 50
	for i in range(ITTERS):
		groups = getGroups(mids, data, k)
		mids = getNewMids(groups, k, n)
	return mids


# recoloring algorithm

def getImgMids(imgObject, k):
	img = imgObject
	img = img.resize((32,32), Image.ANTIALIAS)

	img = img.convert("RGB")
	datas = img.getdata()

	pts = np.array(datas)/255
	fitpts = getFit(pts, k, 3)*255

	return fitpts

def imgRecolor(imgObject, numColors):
	img = imgObject.resize((64, 64), Image.ANTIALIAS)
	mids = getImgMids(imgObject, numColors)
	mids = mids.astype(int)

	# newColors = np.random.rand(numColors, 3)*255
	# newColors = newColors.astype(int)
	newColors = mids # this makes the colors kinda weird

	img = img.convert("RGBA")
	datas = img.getdata()
	newDatas = []

	for item in datas:
		if item[3] < 0.1: # transparent
			newDatas.append((255,255,255,0)) # 0 means transparent
		else: # opaque
			citem = item[0:3]
		nextColor = getMid(citem, mids, numColors)
	# newDatas.append(tuple(mids[nextColor]))
	newDatas.append(tuple(newColors[nextColor]))

	img.putdata(newDatas)
	img = img.resize((3, 3), Image.ANTIALIAS)
	x = np.array(img)
	x = x[:,:,:3].tolist()
	colors.append(x)

	return img

if __name__ == '__main__':
	for i in range(6):
		img = imgRecolor(Image.open("data/b{}.JPG".format(i+1)), 6)
		img.show()
	img.save('coolFace.png')
	with open('data.json', 'w') as f:
		json.dump(colors, f)
