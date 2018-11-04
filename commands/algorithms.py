
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

