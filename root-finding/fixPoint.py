import matplotlib.pyplot as plt
import math

def fixPoint(f, start, a, b, epsilon=1e-10, k=256):
	xs = []
	s = start
	err = 1
	for i in range(k):
		x = f(s)
		err = abs(err - x)
		xs.append(x)
		if err < epsilon:
			break
	return x,xs


f = lambda x: pow(x,1/3)
r,l = fixPoint(f, 0.9, 0, 2)

lis = [f(x) for x in range(10)]
lis2 = [x for x in range(10)]

plt.plot(lis)
plt.plot(lis2)
plt.plot(r,f(r),"o")

print(r,f(r))

plt.show()

