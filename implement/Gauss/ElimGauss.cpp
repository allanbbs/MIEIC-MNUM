#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;


vector<vector<double>> matrix;
vector<double> icog;
vector<double> indep;

void normalizeMatrix(vector<vector<double>> &m){
	col = m.size();
	row = m[0].size();
	pivot = m[0][0];
	for(int i =0;i<col;i++){
		for(int j =0;j<row;j++)
			m[i][j] /= pivot;
	}
	pivot = m[1][0];
	for(int i =0;i<m[1].size();i++){
		m[1][i] -= m[0][i] * pivot;

	}











}
