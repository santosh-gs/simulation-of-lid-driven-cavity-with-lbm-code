def Compute_Fields() :
    global Nodes_X, Nodes_Y, NDir, Density, U, V, C, f, err
    err = 0

    for i in range(Nodes_X) :
        for j in range(Nodes_Y) :
            sum1 = 0; sum2 = 0
            a = U[i][j]; b = V[i][j] # New Line
            for k in range (0, NDir) :
                U[i][j] += f[i][j][k] * C[k][0]
                V[i][j] += f[i][j][k] * C[k][1]
                Density[i][j] += f[i][j][k]
            U[i][j] /= Density[i][j]
            V[i][j] /= Density[i][j]
            sum1 += (U[i][j]-a)**2 + (V[i][j]-b)**2 # Numerator
            sum2 += a**2 + b**2                     # Denominator
    err += sum1/sum2