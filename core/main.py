import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy as sp

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

''' Visualize '''
plt.scatter(x[0][0], x[0][1],color='b', alpha=0.5)
plt.scatter(x[0][0], x[0][2],color='r', alpha=0.5)
plt.scatter(x[0][1], x[0][2],color='g', alpha=0.5)
plt.show()

for j in range(x[0].__len__()):
    mean = sp.mean(x[0][j])
    var = sp.var(x[0][j])
    print "variance of w%d and x%d is %f" % (i, j, var)
    print "mean of w%d and x%d is %f" % (i, j, mean)
    x_axis = np.arange(-12, 12, 0.001)
    plt.plot(x_axis, norm.pdf(x_axis,mean,var), label='set: '+str(j)+' mean ='+ str(mean) + ' var = '+str(var))
plt.legend()
plt.title('Part 1')
plt.show()

print "variance x of w1 and w2 is %f and %f" % (sp.var(x[0][0]), sp.var(x[1][0]))
print "variance y of w1 and w2 is %f and %f" % (sp.var(x[0][1]), sp.var(x[1][1]))
print "variance z of w1 and w2 is %f and %f" % (sp.var(x[0][2]), sp.var(x[1][2]))
print "mean x of w1 and w2 is %f and %f" % (sp.mean(x[0][0]), sp.mean(x[1][0]))
print "mean y of w1 and w2 is %f and %f" % (sp.mean(x[0][1]), sp.mean(x[1][1]))
print "mean z of w1 and w2 is %f and %f" % (sp.mean(x[0][2]), sp.mean(x[1][2]))


