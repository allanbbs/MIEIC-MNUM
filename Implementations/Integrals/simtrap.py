import math


def f(x):
	return math.sqrt(1 + (2.5*math.e**(2.5*x))**2)

def trap(a,b,h):
	soma = f(a) + f(b)
	i = 1
	inter = (b-a)/h
	while(a<b and i < inter):
		soma+=2*f(a+i*h)
		i+=1
	return h/2*soma
	
def simpson(f,h,x0,xn):
	soma = f(x0) + f(xn)
	i = 1
	inter = (xn - x0)/h
	while(x0<xn and i < inter):
		if(i%2 == 0):
			soma+=2*(f(x0+i*h))
		else:
			soma+=4*(f(x0+i*h))
		i+=1
	return h/3*soma

#Calc. integral from list of values i.e discrete function
def simtable(h,table):
	s = table[-1] + table[0]
	for i in range(1,len(table)-1):
		if i % 2:
			s+= table[i]*4
		else:
			s+=table[i]*2
	return h/3*s


def trapduplo(f,a,A,b,B):
	hx = (A-a)/2.0
	hy = (B-b)/2.0
	e0 = f(a,b) + f(A,b) + f(A,B) + f(a,B)
	e1 = f(a+hx,b) + f(a,b+hy) + f(a+hx,B) + f(A,b+hy)
	e2 = f(a+hx,b+hy)
	return ((hx*hy)/4)*(e0 + 2*e1 + 4*e2)
#Function below is used calc. double integral from numeric table
def trapduplotable(a,A,b,B):
	hx = (A-a)/2.0
	hy = (B-b)/2.0
	e0 = 1.1 + 7.7 + 1.2 + 7.3 	#table vertex
	e1 = 1.4+ 2.2 + 1.5 + 2.1 	#middle value from each side
	e2 = 3.1			#value in the middle of the table
	return ((hx*hy)/4)*(e0 + 2*e1 + 4*e2)
'''
print(trapduplotable(0,2,0,2))
table = [0.0000000000,0.0025086954,0.1031391271,0.5542043311,1.7762260341,4.3579346535,9.0562692976,16.7963777650,28.6716165454,45.9435508189,70.0419544565,102.5648100198,145.2783087610,200.1168506233,269.1830442402,354.7477069361,459.2498647263]

tablel = [1.04,0.38,1.08,0.64,0.12]
print(simtable(1,table))
#print("Erro: ",(simtable(0.25,table) - simtable(0.5,tablel))/15)


#print(trap(0.0,1.0,0.125,80))
h = 0.125
print("simpson:")
erro = simpson(f,h/4,0,1) - simpson(f,h/2,0,1)
print(erro/15)
print(simpson(f,0.125,0,1))
print(simpson(f,0.125/2,0,1))
print(simpson(f,0.125/4,0,1))
print("-------")
print("trapezio: ")
erro = trap(0,1,h/4) - trap(0,1,h/2)
print(erro/3)
print(trap(0,1,h/1))
print(trap(0,1,h/2))
print(trap(0,1,h/4))'''

