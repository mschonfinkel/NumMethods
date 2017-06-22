import numpy as np
import matplotlib.pyplot as plt

def Legendre(n, x):
    x = np.array(x)
    if n == 0:
        return x*0 + 1.0
    elif n == 1:
        return x
    else:
        return ((2.0*n-1.0)*x*Legendre(n-1,x)-(n-1)*Legendre(n-2,x))/n

x = np.array([1, 3, 5, 7], dtype = float)
y = np.array([-1, 4, -7, 9], dtype = float)

g = lambda x: x**3

discrete_l1 = np.dot(g(x), g(x))
discrete_l2 = np.dot(y, g(x))

alpha = discrete_l2/discrete_l1

plt.scatter(x,y, marker='o', color='r')

x_linspace = np.linspace(0, 9, 100)

plt.plot(x_linspace, alpha*g(x_linspace))

plt.show()
