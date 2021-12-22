#include <iostream>
#include <string>
using namespace std;

// global variable
const int SIZE = 10;

struct DATE
{
	int month;
	int day;
	int year;
};

// prototype
float average(int grade1, int grade2);

int main()
{
	DATE y; // y is empty so far      INSTANCE!!
	y.month = 12;
	y.day = 25;
	y.year = 2001;

	DATE Lupoli = { 12, 30, 1970 }; // ORDER DOES MATTER!!! INSTANCE!!
	DATE Ryan = { 06, 11, 1984 }; // INSTANCE!!

	return 0;
}
