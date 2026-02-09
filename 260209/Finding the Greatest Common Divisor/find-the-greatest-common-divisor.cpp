#include <iostream>
#include <algorithm>

using namespace std;

int n, m;

void gcd(int n, int m) {
    int small = min(n, m);
    int gcd = small;
    for (int i{small}; i >= 0; --i) {
        if (n % gcd == 0 && m % gcd == 0) {
            break;
        }
        gcd--;
    }

    cout << gcd << '\n';
}

int main() {
    cin >> n >> m;

    gcd(n, m);

    return 0;
}