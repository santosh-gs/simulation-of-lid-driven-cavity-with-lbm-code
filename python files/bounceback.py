def bounceback():
    global Nodes_X, Nodes_Y, Walls, U, V
    for i in range(Nodes_X):
        for j in range(Nodes_Y):
            if Walls[i][j] == 1:
                f[i][j][1], f[i][j][3] = f[i][j][3], f[i][j][1]
                f[i][j][5], f[i][j][7] = f[i][j][7], f[i][j][5]
                f[i][j][2], f[i][j][4] = f[i][j][4], f[i][j][2]
