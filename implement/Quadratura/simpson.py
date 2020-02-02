import math
import numpy as np



	
sll = [1.04,0.37,0.38,1.49,1.08,0.13,0.64,0.84,0.12]
sl  = [1.04,0.38,1.08,0.64,0.12]
def f1(l,h):
	s = 0;
	for i in range(1,len(l)-1):
		if i%2:
			s+=4*l[i]
		else:
			s+=2*l[i]
	return (h/3)*(l[0] + s + l[-1])


print(f1(sll,0.25))
print((f1(sll,0.25)-f1(sl,0.5))/15.0)











'''def f(x,y):
	return 3*x + 2*y'''
def gen(a,b,step):
	while a < b:
		yield a
		a+=step
def g(x):
	return math.sin(x)

def simpson(f,h,x0,xn,n):
	return (h/3)*(f(x0) + f(xn) + 4 *(sum([f(x0 +k*h) for k in range(1,n,2)])) + 2*(sum([f(x0+k*h) for k in range(2,n-1,2)])))




def simpsondouble(f,a,A,b,B,extremos):
	hx = (A-a)/2
	hy = (B-b)/2
	e0 = f(extremos[0], extremos[2]) + f(extremos[0], extremos[3]) + f(extremos[1], extremos[2]) + f(extremos[1], extremos[3])
	e1 = f(extremos[0] + hx, extremos[2]) + f(extremos[0], extremos[2] + hy) + f(extremos[1], extremos[2]+hy) + f(extremos[0]+hx, extremos[3])
	e2 = f(extremos[0]+hx,extremos[2]+hy)
	return ((hx*hy)/9)*(e0 + 4*e1 + 16*e2)

'''
print(simpsondouble(f,0,2,0,2,[0,2,0,2]))
print(simpson(g,0.01963495,0,math.pi/2,80))
'''
#print((f(0.2) - f(0.4))/15)


