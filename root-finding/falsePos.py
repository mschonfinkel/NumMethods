def falsePostion(f, a, b, epsilon1 = 1e-6, epsilon2=1e-6, k=128):
	from random import uniform
	
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