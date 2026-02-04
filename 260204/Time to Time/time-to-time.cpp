#include <iostream>

using namespace std;

int a, b, c, d;

int main() {
    cin >> a >> b >> c >> d;

    int minutes1 = (a * 60) + b;
    int minutes2 = (c * 60) + d;

    cout << minutes2 - minutes1 << '\n';

    return 0;
}