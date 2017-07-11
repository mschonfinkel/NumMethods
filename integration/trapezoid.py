import numpy as np
import matplotlib.pyplot as plt

def trapezoid(f, x, y):
	print(y,x)
	return sum((y[1:] + y[:-1])*(x[1:] - x[:-1]))*0.5

f1 = lambda x: np.exp(x)
f2 = lambda x: np.sqrt(x)

f = f2

a,b = 1, 4

x = np.linspace(0, 8, 200)
y = f(x)

x_ = np.linspace(a, b, 4)
y_ = f(x_)

fig = plt.figure() 
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)

fig.suptitle('Trapezoid Method', fontsize=14, fontweight='bold')

result = trapezoid(f, x_, y_)
print(result)

ax.axis([0, 6, 0, 4])

ax.plot(x, y, lw=2)

ax.fill_between(x_, 0, y_, facecolor='gray', alpha=0.6)

plt.show()
