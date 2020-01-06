import math
from numpy.linalg import inv,norm
import numpy as np
def f1(x,y):
	return math.sin(x+y) - math.e**(x-y)
def f2(x,y):
	return math.cos(x+y) - (x**2)*(y**2)
def f1x(x,y):
	return math.cos(x+y) - math.e**(x-y)
def f1y(x,y):
	return math.cos(x*y) + math.e**(x-y)
def f2x(x,y):
	return -math.sin(x+y) - 2*(x)*(y**2)
def f2y(x,y):
	return -math.sin(x+y) - 2*(y)*(x**2)

def jacobian(x,y):
	return f1x(x,y)*f2y(x,y) - f1y(x,y)*f2x(x,y);
def h(x,y):
	return f1(x,y)*f2y(x,y)-f1y(x,y)*f2(x,y)

def k(x,y):
	return f1x(x,y)*f2(x,y)-f1(x,y)*f2x(x,y)



def newton(f,diff,x,numIt):
		for i in range(numIt):
			x -= f(x) / diff(x)
			print(x)

def sistNewton(x,y,numIt):
	for i in range(numIt):
		xAnt = x
		x -= h(x,y)/jacobian(x,y)
		y -= k(xAnt,y)/jacobian(xAnt,y)
		print('n: {2}\t x: {0:.10f}\t y: {1:.10f} f1(x,y): {3:.10f} f2(x,y): {4:.10f}'.format(x,y,i,f1(x,y),f2(x,y)))
sistNewton(0.250000,0.250000,30)




		
	
