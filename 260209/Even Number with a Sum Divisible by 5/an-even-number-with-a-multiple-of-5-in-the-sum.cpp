#include <iostream>

using namespace std;

void evenDiv5(int a) {
    bool even{a % 2 == 0};
    int sumOfDigits{};
    while (a > 0) {
        sumOfDigits += a % 10;
        a /= 10;
    }

    if (sumOfDigits % 5 == 0 && even) {
        cout << "Yes";
    } else {
        cout << "No";
    }
}

int main() {
    int n;
    cin >> n;

    evenDiv5(n);

    return 0;
}