import numpy
import math


def f(x,y):
	return -0.25*(y-64)



def rk2(f,h,x0,y0,xf):
	x,y=x0,y0
	while x < xf -0.00001:
		x,y = x + h, y + h*f(x+(h/2),y + (h/2)*f(x,y))
	return x,y


def rk4(f,h,x0,y0,xf):
	x,y = x0,y0
	i = 1
	while(x < xf-0.000001):
		d1 = h*f(x,y,z);
		d2 = h*f(x + (h/2),y + (d1/2),z)
		d3 = h*f(x + (h/2),y + (d2/2))
		d4 = h*f(x + h,y + d3)
		dy = d1/6 + d2/3 + d3/3 +d4/6
		x,y = x+h,y+dy
		
		print(str(i) + ": ",x,y)
		
		i+=1
	return x,y

def f(T,C,t):
	return -(pow(math.e,-0.1/(T+273)))*C
def g(T,C,t):
	return 15.0*pow(math.e,-0.1/(T+273))*C -0.1*(T-20)

def second_rk4(f,g,h,x0,y0,z0,xf):
	x,y,z = x0,y0,z0
	i = 1
	while(1):
		dy1,dz1 = h*f(x,y,z),h*g(x,y,z)
		dy2,dz2 = h*f(x + (h/2),y + (dy1/2),z + (dz1/2)),h*g(x + (h/2),y + (dy1/2),z + (dz1/2))
		dy3,dz3 = h*f(x + (h/2),y + (dy2/2),z + (dz2/2)),h*g(x + (h/2),y + (dy2/2),z + (dz2/2))
		dy4,dz4 = h*f(x + h,y + dy3,z + dz3),h*g(x + h,y + dy3,z + dz3)
		dy = dy1/6 + dy2/3 + dy3/3 +dy4/6
		dz = dz1/6 + dz2/3 + dz3/3 +dz4/6
		x,y,z = x + h,y + dy,z + dz
		print(str(i) + ": ",x,y,z)
		if i == 2:
			break
		i+=1

second_rk4(f,g,0.25,0.5,2,20.00,1)
def yll(x,y,yl):
	return  2 + x**2 + x*yl

#second_rk4(yll,0.25,0,1,1,0)

def system_rk4(f,h,x0,y0,yl0,xf):
	pass



def g(x,y):
	return -0.25*(y-64)

#print(rk2(g,0.5,4,0,5))
#print(rk4(g,0.5,4,0,5))
