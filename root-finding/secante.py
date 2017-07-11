import numpy as np
import matplotlib.pyplot as plt
import math

def secante(f,x0,x1,epsilon1 = float("1e-6"),epsilon2 = float("1e-6")):
	if (abs(f(x0)) < epsilon1):
		return x0
	if(abs(f(x1)) < epsilon1):
		return x1

	if(abs(x1 - x0) < epsilon2):
		return x1

	x2 = (x0*f(x1) - x1*f(x0))/(f(x1) - f(x0))

	if(abs(f(x2)) < epsilon1):
		return x2
	if(abs(x2 - x1) < epsilon2):
		return x2	

	return secante(f,x1,x2,epsilon1,epsilon2)

#----------------
x = np.linspace(-20, 20, 400)

#----------------
f = lambda x: np.sin(x) - x

r = secante(f,5,10)
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