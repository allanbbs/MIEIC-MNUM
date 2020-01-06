#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

//Funcoes

double f1(double x, double y)
{
	return 2*x*x -x*y -5*x + 1;
}

double f2(double x, double y)
{
	return x + 3*log(x) - y*y;
}

//Formulacoes de picardPeano
double pp1x(double x, double y)
{
	return sqrt((x*y +5*x -1)/2);
}

double pp2y(double x, double y)
{
	return sqrt(x + 3*log(x));
}


void sistPicardPeanoSeigel(double x, double y, int numIt)
{
	double xAnt,yAnt;

	for (int i = 0; i < numIt; i++)
	{
		xAnt = x;
		yAnt = y;
		cout<<xAnt<< " "<<yAnt<<endl;
		x = pp1x(xAnt, yAnt);
		y = pp2y(x, yAnt);

		cout << "x: " << x << '\t' << "y: " << y << endl;
	}

	cout << "f1 result: " << f1(x, y) << endl;

	cout << "f2 result: " << f2(x, y) << endl;
}

void sistPicardPeano(double x, double y, int numIt)
{
	double xAnt,yAnt;

	for (int i = 0; i < numIt; i++)
	{
		xAnt = x;
		yAnt = y;
		x = pp1x(xAnt, yAnt);
		y = pp2y(x, yAnt);

		
	}
	cout << "x: " << x << '\t' << "y: " << y << endl;

	cout << "f1 result: " << f1(x, y) << endl;

	cout << "f2 result: " << f2(x, y) << endl;
}

int main()
{
	const int OUT_PREC = 5;
	cout << fixed << setprecision(OUT_PREC);
	sistPicardPeano(10, 10, 50);
	sistPicardPeanoSeigel(10,10,50);
	return 0;
}
