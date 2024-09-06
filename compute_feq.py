def Compute_Fields() :
    global Nodes_X, Nodes_Y, NDir, Density, U, V, C, f

    for i in range(Nodes_X) :
        for j in range(Nodes_Y) :
            for k in range (0, NDir) :
                U[i][j] += f[i][j][k] * C[k][0]
                V[i][j] += f[i][j][k] * C[k][1]
                Density[i][j] += f[i][j][k]
            U[i][j] /= Density[i][j]
            V[i][j] /= Density[i][j]