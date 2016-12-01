#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{	
	double cur;
	double high;
	double crit;

	double maxi = -1;
	double mini = 100000;
	double total;
	int d;
	int n;

	n = 0;
	total = 0;

	while(scanf("Core %d: +%lf°C  (high = +%lf°C, crit = +%lf°C)\n",&d,&cur, &high, &crit) != -1) {
		maxi = max(maxi, cur);
		mini = min(mini, cur);
		n++;
		total += cur;
	} 

	cout << "Maximum: " << maxi << endl;
	cout << "Minimum: " << mini << endl;
	cout << "Average: " << total / n << endl;



}

