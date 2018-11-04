import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
print (theta)
z = np.linspace(-2, 2, 100)
print (z)
r = z**2 + 1
# x = r * np.sin(theta)
# y = r * np.cos(theta)
# x = r * np.sin(1)
# y = r * np.cos(1)
x = z * 1
y = x 

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()
