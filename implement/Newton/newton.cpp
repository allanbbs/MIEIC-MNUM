#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

double f(double x,double y)
{
	return 2*x*x -x*y -5*x + 1;
}

double diffFx(double x,double y)
{
	return 4*x -y -5;
}

double diffFy(double x,double y){

	return -x;

}
double f1(double x,double y)
{
	return x + 3*log10(x) -y*y;
}

double diffF1x(double x)
{
	return 1 + 3*(1/x);
}

double diffF1y(double x)
{
	return -2*y;
}

void newton(double f(double,double),double f1(double,double), double diff1x(double,double),double diff1y(double,double),double diff2x(double.double),double diff2y(double,double), double x,double y, int numIt)
{
	double jacobianDet = diff1x(x,y)*diff2y(x,y) - diff1y(x,y)*diff2x(x,y);


























}
void newton1(double f(double),double diff(double), double x, int numIt)
{
	for (int i = 0; i < numIt; ++i)
	{
		x -= f(x) / diff(x);

		cout << "x = " << x << endl;
	}
}

int main()
{
	const int OUT_PREC = 5;
	cout << fixed << setprecision(OUT_PREC);

	newton(f1, diffF1, 3.8, 1);

	return 0;
}
