#include <iostream>

using namespace std;

int power(int a, int b) {
    int mul{1};
    for (int i{}; i < b; ++i) {
        mul *= a;
    }
    return mul;
}

int main() {
    int a, b;
    cin >> a >> b;

    cout << power(a, b);

    return 0;
}