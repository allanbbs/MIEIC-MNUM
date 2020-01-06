#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

//Function
double f(double x)
{
	return x*x*x*x +2*x*x*x -x -1;
}


void falsePosition(double f(double x), double a, double b, int numIt)
{
	double r = 0.5 ;

	for (int i = 0; i < numIt; ++i)
	{
		
		if (f(a) * f(r) < 0)
			b = r;
		else
			a = r;
		r = (a*f(b) - b*f(a))/(f(b)-f(a));
	
	}
	cout<< a<<endl;
	cout<< b<<endl;

}

int main()
{
	int const OUT_PREC = 5;
	cout << fixed << setprecision(OUT_PREC);

	falsePosition(f, 0.0, 0.8, 10);

	return 0;
}
