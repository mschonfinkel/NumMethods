import numpy as np

def Legendre(n, x):
    x = np.array(x)
    if n == 0:
        return x*0 + 1.0
    elif n == 1:
        return x
    else:
        return ((2.0*n-1.0)*x*Legendre(n-1,x)-(n-1)*Legendre(n-2,x))/n

f = Legendre(2, [2,3,4])
print(f)