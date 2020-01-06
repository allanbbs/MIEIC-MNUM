import math

def f(x):
    return math.sin(x)**2;


def bzao():
    return (math.sqrt(5) - 1)/2


def trisec(a,b,tol):
    c = a + (1/3.0)*(b-a)
    d = a + (2/3.0)*(b-a)
    i = tol
    while(i>0):
        if(f(c)>f(d)):
            a = c
            c = a + (1/3.0)*(b-a)
            d = a + (2/3.0)*(b-a)
        else:
            b = d
            c = a + (1/3.0)*(b-a)
            d = a + (2/3.0)*(b-a)
        i-=1
    return [a,b]

a,b = trisec(0.5,4.0,100)
h = ((b-a)/2)
x2 = ((b-a)/2) + a
num = (h*(f(a)-f(b)))
den = 2*(f(b)-2*f(x2)+f(a))
xm = x2 + num/den
ym = f(xm)
print("y minimo: ",ym)
print(xm)

print("Intervalo pos trisec:",trisec(0,10,100))