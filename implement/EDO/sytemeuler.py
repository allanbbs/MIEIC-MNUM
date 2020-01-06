import numpy
import math


def f(T,C,t):
	return -(pow(math.e,-0.1/(T+273)))*C
def g(T,C,t):
	return 15.0*pow(math.e,-0.1/(T+273))*C -0.1*(T-20)

'''def xll(x,y,yl):
	return 2 + x**2 + x*yl'''

def yll(x,y,yl):
	return  2 + x**2 + x*yl



def euler(f,g,h,t0,T0,C0,xf):
	T,C,t = T0, C0 ,t0
	i=1
	while(t < xf - 0.0000001):
		#print(str(i) + ":",T,C,t)
		T,C,t = T + h*g(T,C,t), C + f(T,C,t)*h, t + h
		print(str(i) + ":",T,C,t)
		i+=1
	return C


'''def euler(f,h,yl0,y0,x0,xf):
	z,y,x = yl0, y0 , x0
	i=0
	while(1):
		print(str(i) + ":",x,y,z)
		z,y,x = z + h*yll(x,y,z), y + z*h, x + h
		#print(str(i) + ":",z,y,x)
		if i == 3:
			break
		i+=1
	return 1'''

#euler(yll,0.25,0,1,1,0)
#h = 0.25
print(euler(f,g,0.25,0.5,20.0,2.00,1))
#print((euler(f,g,0.25/4,0.5,20.0,2.00,1))) #C''
'''s = euler(f,g,0.25,0.5,20.0,2.00,1)
sl = euler(f,g,0.25/2,0.5,20.0,2.00,1)
sll = euler(f,g,0.25/4,0.5,20.0,2.00,1)
print((sl-s)/(sll-sl))
print("Erro absoluto: ",sll-sl)'''

#euler(f,g,h/4,0.5,20.00,2.000,0)
#euler(f,g,0.125,0.5,20.00,2.000,0)
#euler(f,g,0.0625,0.5,20.00,2.000,0)