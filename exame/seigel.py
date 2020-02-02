import math




def seigel(x0,y0,z0,w0,numIt):
	x,y,z,w = x0,y0,z0,w0
	i = 1
	while(i<=numIt):
		x = (25-(0.5*y + 3*z + 0.25*w))/6
		y = (10 -(1.2*x + 0.25*z + 0.2*w))/3
		z = (7 -(-x + 0.25*y + 2*w))/4
		w = (-12 -(2*x + 4*y + z)) / 8
		if(i == 1):
			break
		i+=1
	return x,y,z,w


print(seigel(2.12687,2.39858,3.99517,-3.73040,10))

