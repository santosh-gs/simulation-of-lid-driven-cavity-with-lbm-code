def bounceback() :
    global  Nodes_X, Nodes_Y, Walls, U, V
    for i in range(Nodes_X) :
        for j in range(Nodes_Y) :
            if Walls[i][j] == 1 :
                U[i][3] = temp
                temp = V[i][1]
                V[i][1] = U[i][3]
                U[i][2] = temp
                temp = V[i][4]
                V[i][4] = U[i][2]
                U[i][6] = temp
                temp = V[i][8]
                V[i][8] = U[i][6]
                U[i][5] = temp
                temp = V[i][7]
                V[i][7] = U[i][5]