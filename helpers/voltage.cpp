#include <fstream>
#include <iostream>
#include <math.h>
#include <stdio.h>
using namespace std;

int main()
{

	ifstream fcin("result");

	long long mini;
	long long maxi;
	double f;
	long long v1;
	long long v2;
	double xx;
	double yy;

	while(!fcin.eof()) {
		fcin >> f;
		fcin >> v1;
		fcin >> v2;

		xx = v1 * (1.0 / pow(2, 13));
		yy = v2 * (1.0 / pow(2, 13));

		printf("|%.1lf GHz|%.5lf Volt|%.5lf Volt|\n", f,xx,yy);
	}


}

