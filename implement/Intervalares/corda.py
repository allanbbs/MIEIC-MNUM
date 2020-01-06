import math

def f(x):

	return x*x*x*x +2*x*x*x -x -1


def falsePosition(func, a, b,numIt):


	r = 0.5 ;

	for i in range(numIt):
		if (func(a) * func(r) < 0):
			b = r
		else:
			a = r
		r = (a*f(b) - b*f(a))/(f(b)-f(a));
	
	print("a :",a)
	print("b :",b)
	print("root: ",r)


falsePosition(f,0,1,10)


