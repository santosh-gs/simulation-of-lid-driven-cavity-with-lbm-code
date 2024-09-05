def Stream() :
    global Nodes_X, Nodes_Y, f
    
    # Particle 1 (1,0)
    for i in range(0, Nodes_X, 1) :
        for j in range(Nodes_Y-1, 0, -1) :
            f[i][j][1] = f[i][j-1][1]
    
    # Particle 2 (0,1)
    for i in range(Nodes_X-1, 0, -1) :
        for j in range(0, Nodes_Y, 1) :
            f[i][j][2] = f[i-1][j][2]

    # Particle 3 (-1,0)
    for i in range(0, Nodes_X, 1) :
        for j in range(0, Nodes_Y-1, 1) :
            f[i][j][3] = f[i][j+1][3]
    
    # Particle 4 (0,-1)
    for i in range(0, Nodes_X-1, 1) :
        for j in range(0, Nodes_Y, 1) :
            f[i][j][4] = f[i+1][j][4]
    
    # Particle 5 (1,1)
    for i in range(Nodes_X-1, 0, -1) :
        for j in range(Nodes_Y-1, 0, -1) :
            f[i][j][5] = f[i-1][j-1][5]
    
    # Particle 6 (-1,1)
    for i in range(Nodes_X-1, 0, -1) :
        for j in range(0, Nodes_Y-1, 1) :
            f[i][j][6] = f[i-1][j+1][6]
    
    # Particle 7 (-1,-1)
    for i in range(0, Nodes_X-1, 1) :
        for j in range(0, Nodes_Y-1, 1) :
            f[i][j][7] = f[i+1][j+1][7]
    
    # Particle 8 (1,-1)
    for i in range(0, Nodes_X-1, 1) :
        for j in range(Nodes_Y-1, 0, -1) :
            f[i][j][8] = f[i+1][j-1][8]