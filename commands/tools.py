
import numpy as np
from .moves import moves

COLORS = ['G', 'Y', 'B', 'W', 'R', 'O']

def genPerfectCube(): 
    perfectCube = []
    for i in range(len(COLORS)):
        for row in range(3): 
            for col in range(3): 
                perfectCube.append(([i, [row, col]], COLORS[i], True))
    return perfectCube

perfectCube = genPerfectCube()

def rotate(oldcube, command):
    newcube = [np.copy(oldcubei) for oldcubei in oldcube]

    if command == "X": 
        newcube = rotate(oldcube, "R")
        newcube = rotate(newcube, "Mi")
        newcube = rotate(newcube, "Li")

    elif command == "F": 
        newcube[4][:,0] = oldcube[1][2]
        newcube[3][0] = oldcube[4][:,0]
        newcube[5][:,2] = oldcube[3][0]
        newcube[1][2] = oldcube[5][:,2]
    elif command == "Fi": 
        newcube[5][:,2] = oldcube[1][2]
        newcube[3][0] = oldcube[5][:,2]
        newcube[4][:,0] = oldcube[3][0]
        newcube[1][2] = oldcube[4][:,0]
    elif command== "B": 
        newcube[1][0] = oldcube[4][:,2]
        newcube[4][:,2] = oldcube[3][2]
        newcube[3][2] = oldcube[5][:,0]
        newcube[5][:,0] = oldcube[1][0]
    elif command== "Bi": 
        newcube[4][:,2] = oldcube[1][0]
        newcube[3][2] = oldcube[4][:,2]
        newcube[5][:,0] = oldcube[3][2]
        newcube[1][0] = oldcube[5][:,0]
    else: 
        for indpair in moves[command]["indpairs"]:
            newcube[indpair[1]][moves[command]["indflips"]] = oldcube[indpair[0]][moves[command]["indflips"]]

    return newcube

def doFormula(oldcube, formula):
    for move in formula.split():
        oldcube = rotate(oldcube, move)
    return oldcube


