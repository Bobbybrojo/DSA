#include <iostream>

using namespace std;

bool sumOfDigitsEven(int n) {
    int sum{};
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum % 2 == 0;
}

bool isPrime(int n) {
    for (int i{2}; i <= n / 2; ++i) {
        if (n % i == 0) return false;
    }
    return true;
}


int main() {
    int a, b;
    cin >> a >> b;

    int count{};
    for (int i{a}; i <= b; ++i) {
        if (isPrime(i) && sumOfDigitsEven(i)) {
            count++;
        }
    }

    cout << count;

    return 0;
}