import math



def f(x):
	return (math.e**x) -x -5


def diff(x):
	return (math.e**x) -1



def pp1x(x):
	return pow(math.e,x) - 5

def pp2x(x):
	return math.log(5 + x)



def picardPeano(func,guess,n):
	for i in range(n):
		print("Iteration ",i,"Value: ",guess)
		guess = func(guess)
	print(guess)

def newton(func,dev,x,n):
	for i in range(n):
		x -= func(x) / dev(x)
		print(x)

picardPeano(pp1x,-5,11)
print("---")
picardPeano(pp2x,3,11)
print("---")
newton(f,diff,-5,11)

