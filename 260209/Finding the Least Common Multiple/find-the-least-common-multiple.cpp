#include <iostream>
#include <algorithm>

using namespace std;

int n, m;

int lcm(int n, int m) {
    int small = min(n, m);
    int big = max(n, m);

    for (int i{big}; i <= n * m; i += big) {
        if (i % small == 0) {
            return i;
        }
    }
    return -1;
}

int main() {
    cin >> n >> m;

    cout << lcm(n, m) << '\n';

    return 0;
}