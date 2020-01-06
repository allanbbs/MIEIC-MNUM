import math


def f(C,T,t=0):
	return -(pow(math.e,-0.1/(T+273)))*C
def g(C,T,t=0):
	return 15.0*pow(math.e,-0.1/(T+273))*C -0.1*(T-20)


def rk4(f,g,h,t0,T0,C0,xf):
	C,T,t = C0,T0,t0
	i = 1
	while(1):
		
		print(str(i) + ": ",t,C,T)
		if i == 2:
			break
		i+=1
	return 1
rk4(f,g,0.25,0.5,20.00,1.000,0)




