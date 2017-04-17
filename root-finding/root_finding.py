from random import uniform

def bissec(f, a, b, epsilon=1e-6, k=128):
	assert not (f(a)*f(b) > 0)

	for i in range(k):
		mid = (a+b)/2.0
		if abs(a-b) < epsilon:
			return uniform(a, b)
		if f(a)*f(mid) < 0:
			b = mid
		else:
			a = mid
	return mid

def secant(f, a, b, epsilon1 = 1e-6, epsilon2=1e-6, k=128):
	assert not (f(a)*f(b) > 0)

	for i in range(k):
		mid = (a*f(b) - b*f(a))/(f(b) - f(a))
		if abs(a-b) < epsilon1:
			return uniform(a, b)
		elif (abs(f(a)) < epsilon2): 
			return uniform(a,mid)
		elif (abs(f(b)) < epsilon2):
			return uniform(mid, b)

		if f(a)*f(mid) < 0:
			b = mid
		else:
			a = mid
	return mid

f = lambda x: pow(x,3) + x - 6
r = bissec(f, -5, 5)
r2 = secant(f, -5.0, 5.0)

print('Bissection: ' + str(r) + ' ' + str(f(r)))
print('Secant: ' + str(r2) + ' ' + str(f(r2)))