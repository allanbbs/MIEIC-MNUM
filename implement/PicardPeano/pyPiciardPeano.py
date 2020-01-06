import math
def f1(x):
	return math.e**x -x - 3

def g(x):
	return pow(math.e,x) - 3

def g1(x):
	return math.log(3 + x)

def picardPeano(func,guess,numIt):

	for i in range(numIt):
		guess = func(guess)
		print("g -> x =",guess)
	print(f1(guess))





def sistPicardPeano(funcX,funcY,guessX,guessY,numIt):
	for i in range(numIt):
		guessX = funcX(guessX,guessY)
		guessY = funcY(guessX,guessY)
		print("Iteration \tX \t Y")
		print(i,"\t%.5f\t%.5f"%(guessX,guessY))
picardPeano(g1,1,50)
picardPeano(g,1,50)
#INPUT : GUESS = , FUNC =,
#OUTPUT: X = 1

