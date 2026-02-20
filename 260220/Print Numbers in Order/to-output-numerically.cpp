#include <iostream>

using namespace std;

void printNums(int n, int curr) {
    if (curr == 0) {
        cout << '\n';
        return;
    }

    cout << n - curr + 1 << ' ';
    printNums(n, curr - 1);
}

void printNumsReverse(int n) {
    if (n == 0) {
        cout << '\n';
        return;
    }

    cout << n << ' ';
    printNumsReverse(n - 1);
}

int main() {
    int N;
    cin >> N;

    printNums(N, N);
    printNumsReverse(N);

    return 0;
}