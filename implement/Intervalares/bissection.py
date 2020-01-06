import math


def f(x):
	return x**3 -10*math.sin(x) + 5.5




def bissection(f,a,b,numIT):
	i = 0
	if(f(a)*f(b) < 0):
		while(i<numIT):
			x = (a+b)/2
			if f(a) * f(x) < 0:
				b = x
			else:
				a = x
			x = (a+b)/2
			print(i)
			i+=1

			print("A: ",a)
			print("B: ",b)
		print("Root: ", x)
		print(f(x))
			
	else:
		print("No roots in given interval")

bissection(f,1.5,5.6,2)