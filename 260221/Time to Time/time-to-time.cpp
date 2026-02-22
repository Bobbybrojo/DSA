#include <iostream>

using namespace std;

int a, b, c, d;

int main() {
    cin >> a >> b >> c >> d;

    int hours = c - a;
    int minutes = d - b;



    cout << hours * 60 + minutes;

    return 0;
}