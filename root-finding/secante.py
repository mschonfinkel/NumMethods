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

f = lambda x:pow(x,3)+3*x-2

x = secante(f,0,1)

print("Seccant: %.12f \nf(x): %.12g" %  (x,f(x)))