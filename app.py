from flask import Flask, render_template, url_for, request
import json

app = Flask(__name__)

cube = []
# initialize the cube
COLORS = ['G', 'Y', 'B', 'W', 'R', 'O']
for color in COLORS:
    cube.append([[color, color],[color, color]])

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
