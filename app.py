from flask import Flask, render_template, url_for, request
import json
import numpy as np

app = Flask(__name__)

cube = []
# initialize the cube
COLORS = ['G', 'Y', 'B', 'W', 'R', 'O']
for color in COLORS:
    cube.append(np.array([[color, color,color],[color, color,color],[color,color,color]]))
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

def rotate(oldcube, move):
    newcube = [np.copy(oldcubei) for oldcubei in oldcube]
    for indpair in moves[move]["indpairs"]:
        try:
            newcube[indpair[1]][moves[move]["indflips"]] = oldcube[indpair[0]][moves[move]["indflips"]]
        except:
            import pdb; pdb.set_trace()
    return newcube
cube = rotate(cube, 'R')
cube = rotate(cube, 'F')


# for every face on the cube, for every color on the side (2by2 matrix) what face and number of fold out does it correspond to?
# layer 0 is closest to you
faces = {}
faces[0] = [[2,i] for i in range(9)]
faces[1] = [[0, i] for i in range(3)]+[[1, i] for i in range(3)]+[[2, i] for i in range(3)]
faces[2] = [[0,i] for i in range(9)]
faces[3] = [[0, 6+i] for i in range(3)]+[[1, 6+i] for i in range(3)]+[[2, 6+i] for i in range(3)]
faces[4] = [[0, 3*i+2] for i in range(3)]+[[1, 3*i+2] for i in range(3)]+[[2, 3*i+2] for i in range(3)]
faces[5] = [[0, 3*i] for i in range(3)]+[[1, 3*i] for i in range(3)]+[[2, 3*i] for i in range(3)]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cubeData', methods=('POST', 'GET'))
def cubeData():
    global cube
    if request.method == "POST": # alter the cube
        cube = request.json['cubeData'] # something like this
        return "thanks"
    elif request.method == "GET": # retreive the cube
        print(cube)
        layers = [[["A" for k in range(6)] for j in range(9)] for i in range(3)]
        for face in range(6):
            print(faces[face])
            for idx in range(9):
                i = idx // 3; j = idx % 3
                print(faces[face][idx][0], faces[face][idx][1])
                layers[faces[face][idx][0]][faces[face][idx][1]][face] = cube[face][i][j]
        print(layers)
        return json.dumps(layers)

if __name__ == "__main__":
    app.run(debug=True)
