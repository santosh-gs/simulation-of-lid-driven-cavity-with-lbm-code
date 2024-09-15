def LBM():
    start = time.time()
    Allocate_Memory()
    Initialise()
    for t in range(0, Timestep):
        print(t)
        Stream()
        bounceback()
        Compute_Fields()
        U[Nodes_X-1,:] = U_Wall
        V[Nodes_X-1,:] = 0
        compute_feq()
        collision()
        for j in range(0,Nodes_Y):
            for k in range(0,NDir):
                f[Nodes_X-1][j][k] = feq[Nodes_X-1][j][k].copy()

    with open('UV_Serial_Iterations.plt', 'w') as file:
        for i in range(0,Nodes_X):
            for j in range(0,Nodes_Y):
                file.write('\n'+str(round(1*i/Nodes_X,6))+'\t'+str(round(1*j/Nodes_Y,6))+'\t'+str(round(U[j][i]/U_Wall,6))+'\t'+str(round(V[j][i]/U_Wall,6))+'\t'+str(round(Density[j][i],6)))
    file.close()
    end = time.time()
    print(end-start)
    Final_Error = math.sqrt(err)
    print(Final_Error)