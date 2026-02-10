#include <iostream>

using namespace std;

bool isLeapYear(int y) {
    if (y % 100 == 0 && y % 400 != 0) {
        return false;
    }
    return y % 4 == 0;
}

int main() {
    int y;
    cin >> y;

    cout << (isLeapYear(y) ? "true" : "false");

    return 0;
}