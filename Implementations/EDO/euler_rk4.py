import math



def f(x,y,z):
	return 1 + x**2 + x*z
def h(x,y):
	return x*(x/2 + 1)*y**3 + (x+5/2)*y**2 


def g(x,y,z):
	return 30.00*(math.e**(-0.5/(y+273)))*y-0.5*(T-20)

def sup(x,y,z):
	return z


def syseuler(x0,y0,z0,h,xf):
	x,y,z = x0,y0,z0
	while(abs(xf-x)>0.00001):
		x,y,z = x + h,y + h*f(x,y,z),z + g(x,y,z)
		print("x:",x)
		print("y:",y)
		print("z:",z)
	return T

def superioreuler(x0,y0,z0,h,xf):
	x,y,z = x0,y0,z0
	while(abs(xf-x)>0.00001):
		x,y,z = x + h,y + h*z,z + h*f(x,y,z)
		print("x:",x)
		print("y:",y)
		print("z:",z)
	return y



def rk4(x0,y0,step,xf):
	x,y = x0,y0
	while(abs(xf-x)>0.00001):
		dy1 = step*h(x,y)
		dy2 = step*h(x + step/2,y + dy1/2)
		dy3 = step*h(x + step/2,y + dy2/2)
		dy4 = step*h(x + step,y + dy3)
		dy = dy1/6 + dy2/3 + dy3/3 + dy4/6
		x,y = x + step,y +dy
		print(x,y)
	return y







def sysrk4(t0,T0,C0,h,xf):
	t,T,C = t0,T0,C0
	while(abs(xf-t)>0.00001):
		dT1,dC1 = h*g(t,T,C),h*f(t,T,C)
		dT2,dC2 = h*g(t+h/2,T + dT1/2,C + dC1/2),h*f(t+h/2,T + dT1/2,C + dC1/2)
		dT3,dC3 = h*g(t+h/2,T + dT2/2,C + dC2/2),h*f(t+h/2,T + dT2/2,C + dC2/2)
		dT4,dC4 = h*g(t+h,T + dT3,C + dC3),h*f(t+h,T + dT3,C + dC3)
		dT,dC = dT1/6 + dT2/3 + dT3/3 + dT4/6,dC1/6 + dC2/3 + dC3/3 + dC4/6
		t,T,C = t + h, T + dT,C + dC
		print(t,T,C)


def superiorrk4(x0,y0,z0,h,xf):
	x,y,z = x0,y0,z0
	while(abs(xf-x)> 0.00001):
		dy1,dz1 = h*sup(x,y,z),h*f(x,y,z)
		dy2,dz2 = h*sup(x+h/2,y + dy1/2,z + dz1/2),h*f(x+h/2,y + dy1/2,z + dz1/2)
		dy3,dz3 = h*sup(x+h/2,y + dy2/2,z + dz2/2),h*f(x+h/2,y + dy2/2,z + dz2/2)
		dy4,dz4 = h*sup(x+h,y + dy3,z + dz3),h*f(x+h,y + dy3,z + dz3)
		dy,dz = dy1/6 + dy2/3 + dy3/3 + dy4/6,dz1/6 + dz2/3 + dz3/3 + dz4/6
		x,y,z = x + h, y + dy,z + dz
		print(x,y,z)


r = rk4(1,0.15,0.1,2.0)
rl = rk4(1,0.15,0.1/2.0,2)
rll = rk4(1,0.15,0.1/4.0,2)
qc = (rl-r)/(rll-rl)
erro = (rll-rl)/15.0
print(qc)
print(erro)
#syseuler(2,2,0.25,2.75)
#superioreuler(1,1,0,0.25,2)
#superiorrk4(0,1,2,0.25,0.5)