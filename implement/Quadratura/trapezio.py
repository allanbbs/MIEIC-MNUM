import math
import numpy as np



def f(x):
	return math.sin(x)

def trap(f,h,x0,xn,n):
	return (h/2)*(f(x0) + f(xn) + 2* sum([f(x0 +k*h) for k in range(1,n)]))

def trapduplo(f,a,A,b,B,extremos):
	hx = (A-a)/2
	hy = (B-b)/2
	e0 = f(extremos[0], extremos[2]) + f(extremos[0], extremos[3]) + f(extremos[1], extremos[2]) + f(extremos[1], extremos[3])
	e1 = f(extremos[0] + hx, extremos[2]) + f(extremos[0], extremos[2] + hy) + f(extremos[1], extremos[2]+hy) + f(extremos[0]+hx, extremos[3])
	e2 = f(extremos[0]+hx,extremos[2]+hy)
	return ((hx*hy)/4)*(e0 + 2*e1 + 4*e2)


table = []
def trapduplotable(a,A,b,B,table):
	hx = (A-a)/2
	hy = (B-b)/2
	e0 = 1.1 + 7.3 + 7.7 + 1.2
	e1 = 1.4 +2.1 + 2.2 + 1.5
	e2 = 3.1
	return ((hx*hy)/4)*(e0 + 2*e1 + 4*e2)

print(trapduplotable(0,2,0,2,table))





print("Resultado: ",trap(f,0.01963495,0,math.pi/2,80))
print("Erro absoluto: ",(trap(f,0.01963495/4,0,math.pi/2,80*4) -trap(f,0.01963495/2,0,math.pi/2,80*2))/3 )
print("Erro absoluto: ",1-(trap(f,0.01963495,0,math.pi/2,80)))
#print(trap(f,(2-0)/80,0,2,80))
#print("Calculated error: ",(1-trap(f,0.5/4,0,2,4)))
#print(trap_error(0,math.pi/2,80,0.01963495))
#print(trapduplo(f,0,2,0,2,[0,2,0,2]))