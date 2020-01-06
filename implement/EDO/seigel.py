import math
import numpy




def seigel1(x0,y0,z0,w0):
	x,y,z,w = z0,y0,z0,w0
	i = 1
	while(1):
		x = (25 - (0.5*y + 3*z + 0.25*w))/6
		y = (10- (1.2*x + 0.25*z + 0.2*w))/3
		z = (7-(-x + 0.25*y +2*w))/4
		w = (-12-(2*x+4*y+z))/8
		print(str(i) + ": ",x,y,z,w)
		if(i==2):
			break
		i+=1
def seigel2(x0,y0,z0,w0):
	x,y,z,w = z0,y0,z0,w0
	i = 1
	while(1):
		x = (25 - (0.5*y + 3*z + 0.25*w))/6
		y = (10- (1.2*x + 0.25*z + 0.2*w))/3
		z = (7-(-x + 0.25*y +2*w))/4
		w = (-12-(2*x+4*y+z))/8
		print(str(i) + ": ",x,y,z,w)
		if(i==2):
			break
		i+=1
seigel1(2.83865,2.22131,4.17630,-3.84236)