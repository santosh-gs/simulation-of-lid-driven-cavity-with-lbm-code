def collision():
      global Nodes_X, Nodes_Y, NDir, f, feq, Relaxation_Time
      for i in range(0, Nodes_X):
        for j in range(0, Nodes_Y):
          for k in range(0, NDir):
            f[i][j][k] = f[i][j][k]-((f[i][j][k]- feq[i][j][k])/Relaxation_Time)
      return f