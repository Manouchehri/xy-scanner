# Python-matplotlib Commands
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import pickle

scanData = pickle.load(open('scanData.p', 'rb'))

#maxfreq = np.amax(scanData, axis=2)
maxfreq = np.zeros((20,40))
for x in range(0, 20):
    for y in range(0, 40):
        maxfreq[x][y] = max(scanData[x][y][94:98])

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(0, 20, 1)
Y = np.arange(0, 40, 1)
X, Y = np.meshgrid(X, Y)

Z = maxfreq.T
#R = np.zeros((20, 40))


Gx, Gy = np.gradient(Z) # gradients with respect to x and y
G = (Gx**2+Gy**2)**.5  # gradient magnitude
N = G/G.max()  # normalize 0..1
surf = ax.plot_surface(
    X, Y, Z, rstride=1, cstride=1, cmap=cm.jet, #facecolors=cm.jet(N)
    linewidth=0, antialiased=False, shade=False)
plt.show()

    