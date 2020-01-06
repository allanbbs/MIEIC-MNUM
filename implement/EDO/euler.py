import numpy as np
import math


def f(x,y):
	return x-2
def g(x,y):
	return -0.25*(y-64)
def euler(f,h,x0,y0,xf):
	x,y = x0,y0
	i = 0
	while(x<xf-0.00001):
		x,y = x+h,y + h*f(x,y)
		print(str(i),"x : ",x," y: ",y)
		i+=1
	return (x,y)
'''s = euler(f,1,0,3,5)[1]
sl = euler(f,0.5,0,3,5)[1]
sll = euler(f,0.25,0,3,5)[1]
qc = (sl-s)/(sll-sl)
erro = sll - sl


print(euler(f,1,0,3,5),5.5 - euler(f,1,0,3,5)[1])
print(euler(f,0.5,0,3,5),5.5 - euler(f,0.5,0,3,5)[1])
print(euler(f,0.25,0,3,5),5.5 - euler(f,0.25,0,3,5)[1])'''

print("Ex :",euler(g,0.5,4,0,5)) #PENULTIMO EXERCICO DO TESTE DE 2016 - CORRECTO





	