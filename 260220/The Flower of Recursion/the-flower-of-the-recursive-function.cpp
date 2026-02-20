#include <iostream>

using namespace std;

void printFlower(int n, int curr) {
    if (curr < n) {
        cout << n - curr << ' ';
        printFlower(n, curr + 1);
    } 
    if (curr == 2 * n) {
        cout << curr - n;
        return;
    }
    if (curr > n) {
        cout << curr - n << ' ';
        printFlower(n, curr + 1);
    }
    if (curr == n) {
        printFlower(n, curr + 1);
    }
}

int main() {
    int N;
    cin >> N;

    printFlower(N, 0);

    return 0;
}