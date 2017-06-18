from collections import namedtuple
import matplotlib.pyplot as plt
import numpy as np

point = namedtuple('Point', 'x y')

L = [point(-1.0, 5.0), point(0.0, 6.0), point(1.0, 11.0), point(2.0, -14.0)]

def lagrange_iter(c : float, L : [point]) -> float:
	result = 0.0
	n = len(L)
	for i in range(n):
		prod = L[i].y
		for j in range(n):
			if i != j:
				prod = prod*(c - L[j].x)/(L[i].x - L[j].x)
		result += prod
	return result

x = np.linspace(-1.5, 2.5, 50)
y = lagrange_iter(x, L)

plt.plot(x, y)

plt.plot(L[0].x, L[0].y, marker='o', color='r')
plt.plot(L[1].x, L[1].y, marker='o', color='r')
plt.plot(L[2].x, L[2].y, marker='o', color='r')
plt.plot(L[3].x, L[3].y, marker='o', color='r')

plt.show()
