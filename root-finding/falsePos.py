from random import uniform
import numpy as np
import matplotlib.pyplot as plt

def falsePostion(f, a, b, epsilon1 = 1e-6, epsilon2=1e-6, k=128):
	from random import uniform
	
	assert not (f(a)*f(b) > 0)

	for i in range(k):
		mid = (a*f(b) - b*f(a))/(f(b) - f(a))
		if abs(a-b) < epsilon1:
			return mid
		elif (abs(f(a)) < epsilon2):
			return mid
		elif (abs(f(b)) < epsilon2):
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

r = falsePostion(f,0,np.pi)
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