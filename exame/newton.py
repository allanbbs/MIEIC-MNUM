import math

def f(x,y):
	return x**2 -y -2

def g(x,y):
	return -x +y**2 -2

def fx(x,y):
	return 2*x
def fy(x,y):
	return -1
def gx(x,y):
	return -1
def gy(x,y):
	return 2*y



def jacobian(x,y):
	return fx(x,y)*gy(x,y) - fy(x,y)*gx(x,y)

def h(x,y):
	return -(f(x,y)*gy(x,y) - fy(x,y)*g(x,y))
def k(x,y):
	return -(fx(x,y)*g(x,y) - f(x,y)*gx(x,y) )

def sisNewton(x,y,numIt):
	i = 0
	while(i<numIt):
		xAnt = x
		x += h(x,y)/jacobian(x,y)
		y += k(xAnt,y)/jacobian(xAnt,y)
		print(x,y)
		i+=1
sisNewton(1.5,0.8,10)
