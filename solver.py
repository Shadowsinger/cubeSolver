
# 2x2 Rubik's Cube Solver
# Authors: Alek and Max
# https://www.youcandothecube.com/solve-it/2-x-2-solution

import numpy as np
from pprint import pprint
#  import requests

cube = []
COLORS = ['G', 'Y', 'B', 'W', 'R', 'O']
for color in COLORS:
    cube.append(np.array([[color, color, color],[color, color, color],[color, color, color]]))

# indpairs specifies what side goes to what side
# ind flips is the indices on those sides to flip
# ie for R turn the first column of 1 into the first column of 0
"""
   [0]
[5][1][4]
   [2]
   [3]
On all faces this is what it looks like in terms of indices
[00 01 02]
[10 11 12]
[20 21 22]
"""
moves = {
        "M":  {"indpairs":[(1,0),(2,1),(3,2),(0,3)], "indflips":([0,1,2],1)},
        "Mi": {"indpairs":[(0,1),(1,2),(2,3),(3,0)], "indflips":([0,1,2],1)},
        "R":  {"indpairs":[(1,0),(2,1),(3,2),(0,3)], "indflips":([0,1,2],2)},
        "Ri": {"indpairs":[(0,1),(1,2),(2,3),(3,0)], "indflips":([0,1,2],2)},
        "U":  {"indpairs":[(0,4),(5,0),(2,5),(4,2)], "indflips":(0)},
        "Ui": {"indpairs":[(4,0),(0,5),(5,2),(2,4)], "indflips":(0)},
        "L":  {"indpairs":[(0,1),(1,2),(2,3),(3,0)], "indflips":([0,1,2],0)},
        "Li": {"indpairs":[(1,0),(2,1),(3,2),(0,3)], "indflips":([0,1,2],0)},
        "F":  {"indpairs":[(1,4),(4,3),(3,5),(5,1)], "indflips":(2)},
        "Fi": {"indpairs":[(4,1),(3,4),(5,3),(1,5)], "indflips":(2)},
        "B":  {"indpairs":[(4,1),(3,4),(5,3),(1,5)], "indflips":(0)},
        "Bi": {"indpairs":[(1,4),(4,3),(3,5),(5,1)], "indflips":(0)},
        "D":  {"indpairs":[(4,0),(0,5),(5,2),(2,4)], "indflips":(2)},
        "Di": {"indpairs":[(0,4),(5,0),(2,5),(4,2)], "indflips":(2)}
        }

algs = {}
algs["Fish_1"] = ['R','U','Ri','U','R','U','U','Ri']
algs["Fish_2"] = algs["Fish_1"]+['U']+['U']+algs["Fish_1"]
algs["The_Cat(Website case 5)"] = algs["Fish_1"]+['U']+algs["Fish_2"]
algs["Diagonal(Website case 7)"] = algs["Fish_1"]+algs["Fish_2"]
algs["The_double_sides(Website case 2)"] = algs["Fish_1"]+algs["Fish_1"]
algs["(Website case 3)"] = algs["Fish_1"]+['U']+algs["Fish_1"]
algs["(Webiste case 6)"] = algs["Fish_1"]+['Ui']+["Fish_2"]
algs["Diagonal PLL"] = ['Ri','F','Ri','B','B','R','Fi','Ri','B','B','R','R']
algs["Parralel PLL switch"] = algs["Diagonal PLL"]+['Ui']

algs['upRotation'] =   ['R', 'Li']
algs['sideRotation'] = ['U', 'Di']
algs['frontRotation'] = ['F', 'Bi']

tmp = []
for i in range(len(COLORS)):
    for row in range(3): 
        for col in range(3): 
            tmp.append(([i, [row, col]], COLORS[i], True))

def rotate(oldcube, move):
    newcube = [np.copy(oldcubei) for oldcubei in oldcube]
    for indpair in moves[move]["indpairs"]:
        newcube[indpair[1]][moves[move]["indflips"]] = oldcube[indpair[0]][moves[move]["indflips"]]
    return newcube

def doFormula(oldcube, formula):
    for move in formula:
        oldcube = rotate(oldcube, move)
    return oldcube


pprint(cube)
print("---------")
cube = doFormula(cube, "RF")
pprint(cube)

