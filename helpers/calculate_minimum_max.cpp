#include <fstream>
#include <iostream>
using namespace std;

int main()
{

	ifstream fcin("output");

	long long mini;
	long long maxi;
	long long x;
	long long y;
	
	maxi = -1;
	mini = 122222222;
	while(!fcin.eof()) {
		fcin >> x;
		fcin >> y;
		maxi = max(y, maxi);
		mini = min(y, mini);
		cout << x << " " << y << endl;
	}

	cout << maxi << " " << mini << endl;

}

