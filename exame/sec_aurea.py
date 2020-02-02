import math


B = 0.6180339887
A = B*B



def f(x):
	return 5*math.cos(x) -math.sin(x)



x1 = 2.0
x2 = 4.0
x3 = A*(x2-x1) + x1
x4 = B*(x2-x1) + x1
def sec_aurea(x1,x2,x3,x4):
	i = 0
	while(abs(x1-x4) > 0.00001 and abs(x2-x3) > 0.00001):
		print("Iteracao ",i," x1: ",x1," x2 : ",x2," x3 : ",x3," x4: ",x4)
		print(f(x1),f(x2),f(x3))
		if f(x3) < f(x4):
			x2 = x4
			x4 = x3
			x3= B*(x4 - x1) + x1
		elif f(x3) > f(x4):
			x1 = x3
			x3 = x4
			x4 = B*(x2 - x3) + x3
		i+=1
	print(f(x3))
	print(f(x4))

sec_aurea(x1,x2,x3,x4)

