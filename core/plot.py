import numpy as np
from mpl_toolkits.mplot3d import Axes3D
'''
import matplotlib
matplotlib.use('GTKAgg')'''
import matplotlib.pyplot as plt

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


def foo(xl,xu):
    p = 1.0/((xu-xl)**2)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    res = .01
    x = y = np.arange(-6,6+res, res)
    X, Y = np.meshgrid(x, y)
    '''for x,y in zip(np.ravel(X), np.ravel(Y)):
        print(x,y,xl<=x<=xu and xl<=y<=xu)'''
    zs = np.array([[0, p][xl <= x <= xu and xl <= y <= xu] for x, y in zip(np.ravel(X), np.ravel(Y))])
    zs = zs/sum(zs)
    # zs=zs/((xu-xl)/res)
    Z = zs.reshape(X.shape)
    print(sum(sum(Z)))
    # print(sum(zs),x,y,Z)
    # ax.plot_surface(X, Y, Z)
    ax.plot_surface(X, Y, Z) # rstride=int((1/res)), cstride=int((1/res)))
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()
foo(-3.3,-.2)