import numpy as np

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