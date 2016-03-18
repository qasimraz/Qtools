import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.stats
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


x = np.array([
    [
        [0.42, -0.2, 1.3, 0.39, -1.6, -0.029, -0.23, 0.27, -1.9, 0.87],
        [-0.087, -3.3, -0.32, 0.71, -5.3, 0.89, 1.9, -0.3, 0.76, -1.0],
        [0.58, -3.4, 1.7, 0.23, -0.15, -4.7, 2.2, -0.87, -2.1, -2.6]
    ],
    [
        [-0.4, -0.31, 0.38, -0.15, -0.35, 0.17, -0.011, -0.27, -0.065, -0.12],
        [0.58, 0.27, 0.055, 0.53, 0.47, 0.69, 0.55, 0.61, 0.49, 0.054],
        [0.089, -0.04, -0.035, 0.011, 0.034, 0.1, -0.18, 0.12, 0.0012, -0.063]
    ],
    [
        [0.83, 1.1, -0.44, 0.047, 0.28, -0.39, 0.34, -0.3, 1.1, 0.18], 
        [1.6, 1.6, -0.41, -0.45, 0.35, -0.48, -0.079, -0.22, 1.2, -0.11], 
        [-0.014, 0.48, 0.32, 1.4, 3.1, 0.11, 0.14, 2.2, -0.46, -0.49, ], 
    ]
],)

''' Part 1 a '''

for i in range(x.__len__()):
    for j in range(x[i].__len__()):
        # mean = np.sum(x[i][j]) / len(x[i][j])
        print "variance of w%d and x%d is %f" % (i, j, sp.var(x[i][j]))
        print "mean of w%d and x%d is %f" % (i, j, sp.mean(x[i][j]))

''' Part 1 b '''
# N = range(2, 11, 1)

# res = 0.1
#
#
#
# def func(xl, xu, res):
#     arr = np.array([[0,0,0]])
#     for x0 in np.arange(xl[0], xu[0]+res, res):
#         for x1 in np.arange(xl[1], xu[1]+res, res):
#             v = 0
#             if xl[0] <= x0 <= xu[0] and xl[1] <= x1 <= xu[1]:
#                 v = float(1.0/(abs(xu[0]-xl[0])*abs(xu[1]-xl[1])))
#             else:
#                 print "WTF"
#             arr = np.append(arr, [[x0, x1, v]], axis=0)
#     return arr
#
# arr=func(xl,xu,res)
#
# X=np.arange(-6,6,0.1)
# Y=np.arange(-6,6,0.1)
#
# x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
# y = x.copy()
# z = np.cos(x ** 2 + y ** 2)
#
# fig = plt.figure()
# ax = plt.axes(projection='3d')
#
# ax.plot_surface(x, y, z, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0)


x0 = np.outer(np.linspace(-6, 6, 100), np.ones(100))
x1 = x0.copy().T


def func(xl, xu):
    x0 = np.outer(np.linspace(-6, 6, 100), np.ones(100))
    x1 = x0.copy()
    xa = min(xl, xu)
    xu = max(xl, xu)
    xl = xa
    z = np.outer(np.linspace(-6, 6, 100), np.zeros(100))
    p = 1.0/((xu-xl)**2)

    return z
z = func(-6, 6)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x0, x1, z, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0)