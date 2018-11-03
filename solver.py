
# 2x2 Rubik's Cube Solver
# Authors: Alek, Max, Kevin

import numpy as np
from pprint import pprint
from commands.moves import moves
from commands.algorithms import algs
from commands.tools import rotate, doFormula, COLORS, perfectCube

cube = []
for color in COLORS:
    cube.append(np.array([[color, color, color],[color, color, color],[color, color, color]]))

cube = doFormula(cube, "X")
pprint(cube)

states = {
    "Fish_1": [([1, [1,0]], "Y", True)]
}

