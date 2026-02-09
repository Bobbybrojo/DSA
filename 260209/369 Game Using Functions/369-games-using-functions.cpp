#include <iostream>
#include <algorithm>

using namespace std;

bool contains369(int n) {
    int tsn[3] = {3, 6, 9};
    while (n > 0) {
        if (find(tsn, tsn + 3, n % 10) != tsn + 3) {
            return true;
        }
        n /= 10;
    }
    return false;
}

int count369(int a, int b) {
    int count{};
    for (int i{a}; i <= b; ++i) {
        if (i % 3 == 0 || contains369(i)) {
            count++;
        }
    }
    return count;
}

int main() {
    int a, b;
    cin >> a >> b;

    cout << count369(a, b);

    return 0;
}