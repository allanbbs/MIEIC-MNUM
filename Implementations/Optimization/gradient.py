import math



def f(x,y):
	return -1.1*x*y + 12*y +7*(x*x) -8*x
def fx(x,y):
	return -1.1*y + 14*x -8
def fy(x,y):
	return -1.1*x + 12

def gradient(x,y,h):
	i = 1
	xn = x - h*fx(x,y)
	yn = y - h*fy(x,y)
	while(abs(xn-x) > 0.000001 and abs(yn-y)>0.000001):
		xn = x - h*fx(x,y)
		yn = y - h*fy(x,y)
		value = f(x,y)
		new_value = f(xn,yn)

		if new_value>value:
			h/=2
		else:
			print(xn,yn)
			print(i,f(xn,yn))
			x = xn
			y = yn
			h*=2
		i+=1
gradient(3.0,1.0,0.1)