import matplotlib.pyplot as plt
import numpy as np

def fixPoint(f, x, g, epsilon1 = 1e-6, epsilon2 = 1e-6, k = 512):
	xs = []
	for i in range(k):
		if abs(f(x)) < epsilon1:
			return x, xs
		x1 = g(x)
		if abs(f(x1) < epsilon1):
			return x1, xs
		if abs(x1 - x) < epsilon2:
			return x1, xs
		x = x1
		xs.append((x, g(x)))
	return x1, xs

#----------------
x = np.linspace(-20, 20, 400)

#----------------
f = lambda x: pow(x, 3) - x + 1
g = lambda x: pow(1-x,1/3.0)

r, xs = fixPoint(f, 0.5, g)
print(r, f(r))

f_np = lambda x: x**3 - x + 1
y_f = x**3 - x + 1

#---------------
fig, ax = plt.subplots()

ax.plot(x, y_f)
ax.plot(x, x)

ax.set_aspect('equal')
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set_ylim([-15,15])
ax.set_xlim([-15, 15])

ax.plot(r, g(r), "o",color="r")

plt.show()