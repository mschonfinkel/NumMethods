def fixPoint(f, start, a, b, epsilon=1e-6, k=128):
	# making a guess in (a,b)
	s = start
	err = 1
	for i in range(k):
		x = f(s)
		err = abs(err - x)
		if err < epsilon:
			break
	return x

'''
f = lambda x: pow(x, 2) - x + 1
r = fixPoint(f, 0.9, 0, 2)

print(r, f(r))
'''