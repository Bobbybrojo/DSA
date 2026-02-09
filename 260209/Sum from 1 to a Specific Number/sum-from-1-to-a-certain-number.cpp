#include <iostream>

using namespace std;

int N;


int sumTo(int n) {
    int sum{};
    for (int i{1}; i <= n; ++i) {
        sum += i;
    }

    return sum / 10;
}

int main() {
    cin >> N;

    cout << sumTo(N);

    return 0;
}