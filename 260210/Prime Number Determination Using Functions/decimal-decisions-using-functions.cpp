#include <iostream>

using namespace std;

bool isPrime(int n) {
    for (int i{2}; i <= n / 2; ++i) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int sumOfPrimes(int a, int b) {
    int sum{};
    for (int i{a}; i <= b; ++i) {
        if (isPrime(i)) {
            sum += i;
        }
    }

    return sum;
}


int main() {
    int a, b;
    cin >> a >> b;

    cout << sumOfPrimes(a, b);

    return 0;
}