from random import uniform
import numpy as np
import matplotlib.pyplot as plt

def bissec(f, a, b, epsilon=1e-6, k=128):
	assert not (f(a)*f(b) > 0)

	for i in range(k):
		mid = (a+b)/2.0
		if abs(a-b) < epsilon:
			return mid
		if f(a)*f(mid) < 0:
			b = mid
		else:
			a = mid
	return mid

#----------------
x = np.linspace(-20, 20, 400)

#----------------
f = lambda x: np.sin(x) - x

r = bissec(f,0,np.pi/2)
print(r, f(r))

y_f = f(x)

#---------------
fig, ax = plt.subplots()

ax.plot(x, y_f)
ax.set_aspect('equal')
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set_ylim([-15,15])
ax.set_xlim([-15, 15])

ax.plot(r, f(r), "o",color="r")
plt.show()