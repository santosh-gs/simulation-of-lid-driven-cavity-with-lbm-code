import numpy as np
data = np.loadtxt('UV_Cython.plt')
x, y, u, v, rho = data.T

# Quiver plot for velocity field
import matplotlib.pyplot as plt
plt.quiver(x, y, u, v)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Velocity Field")
plt.show()
