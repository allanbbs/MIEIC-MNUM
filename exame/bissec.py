import math

def f(x):
	return math.e**(0.7*x) -x**2 - 0.5


def bissec(f,a,b,n):

	if (f(a) * f(b) < 0):
		while(abs(a-b)>0.00001):
			x = (a+b)/2.0
			print("Root: ",x,"A: ",a,"B: ",b)
			if f(a) * f(x) < 0:
				b = x
			else:
				a = x
			x = (a+b)/2.0
		print("Root: ",x,"A: ",a,"B: ",b)
	else:
		printf("No root in interval")

bissec(f,-1,0,2)