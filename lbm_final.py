import numpy as np
import math
import time

def Allocate_Memory():
    global Nodes_X, Nodes_Y, NDir, Timestep, U_Wall, Initial_Density, U, V, Density, f, feq, Walls, C, Weight, Reynolds_Number, Kinematic_Viscocity, Relaxation_Time

    Reynolds_Number = 50
    Timestep = 50
    Nodes_X = 30
    Nodes_Y = 30
    NDir = 9 
    U_Wall = 0.1
    Initial_Density = 2.7
    Kinematic_Viscocity = (Nodes_X*U_Wall)/Reynolds_Number
    Relaxation_Time = (6*Kinematic_Viscocity+1)/2
    
    f = np.zeros((Nodes_X, Nodes_Y, NDir), float)
    feq = np.zeros((Nodes_X, Nodes_Y, NDir), float)
    Walls = np.zeros((Nodes_X, Nodes_Y), float)
    Density = np.zeros((Nodes_X, Nodes_Y), float)
    U = np.zeros((Nodes_X, Nodes_Y), float)
    V = np.zeros((Nodes_X, Nodes_Y), float)
    Weight = np.array([4/9, 1/9, 1/9, 1/9, 1/9, 1/36, 1/36, 1/36, 1/36])
    C = np.array([[0,0],[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]])

def Initialise():
    global Nodes_X, Nodes_Y, U, V, Initial_Density, Density, f, feq, Walls

    U.fill(0)
    V.fill(0)
    Density.fill(Initial_Density)
    Walls[0,:] = Walls[Nodes_Y-1,:] = Walls[:,0] = Walls[:,Nodes_X-1] = 1
    compute_feq()
    f = feq.copy()

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

def bounceback():
    global Nodes_X, Nodes_Y, Walls, U, V
    for i in range(Nodes_X):
        for j in range(Nodes_Y):
            if Walls[i][j] == 1:
                f[i][j][1], f[i][j][3] = f[i][j][3], f[i][j][1]
                f[i][j][5], f[i][j][7] = f[i][j][7], f[i][j][5]
                f[i][j][2], f[i][j][4] = f[i][j][4], f[i][j][2]

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

def compute_feq():
      global Nodes_X, Nodes_Y, NDir, f, feq, U, V, C, Initial_Density, Weight
      for i in range(0, Nodes_X):
        for j in range(0, Nodes_Y):
          for k in range(0,NDir):
            CdotU = C[k][0] * U[i][j] +  C[k][1]* V[i][j]
            feq[i][j][k] = Density[i][j]*Weight[k]*(1 + 3*(CdotU) + 4.5*(math.pow(CdotU,2)) - 1.5*(math.pow(U[i][j],2) + math.pow(V[i][j],2)))
      return feq

def collision():
      global Nodes_X, Nodes_Y, NDir, f, feq, Relaxation_Time
      for i in range(0, Nodes_X):
        for j in range(0, Nodes_Y):
          for k in range(0, NDir):
            f[i][j][k] = f[i][j][k]-((f[i][j][k]- feq[i][j][k])/Relaxation_Time)
      return f

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

LBM()