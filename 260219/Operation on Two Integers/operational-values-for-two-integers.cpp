#include <iostream>

using namespace std;

void operation(int &a, int &b) {
    if (a < b) {
        b += 25;
        a *= 2;
    } else {
        b *= 2;
        a += 25;
    }
}

int main() {
    int a, b;
    cin >> a >> b;

    operation(a, b);

    cout << a << ' ' << b;

    return 0;
}