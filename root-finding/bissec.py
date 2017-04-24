def bissec(f, a, b, epsilon=1e-6, k=128):
	from random import uniform

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