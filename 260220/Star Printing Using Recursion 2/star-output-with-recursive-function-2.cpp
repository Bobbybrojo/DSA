#include <iostream>

using namespace std;

void printStars(int n, int curr) {
    if (curr > 2 * n) return;
    if (curr == n) printStars(n, curr + 1);
    else {
        int amt = curr < n ? n - curr : curr - n;
        for (int i{}; i < amt; ++i) {
            cout << '*' << ' ';
        }
        cout << '\n';

        printStars(n, curr + 1);
    }
}

int main() {
    int n;
    cin >> n;

    printStars(n, 0);

    return 0;
}