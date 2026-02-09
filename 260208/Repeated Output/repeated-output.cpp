#include <iostream>

using namespace std;

int N;

void printLines(int n) {
    for (int i{}; i < n; ++i) {
        cout << "12345^&*()_" << '\n';
    }
}

int main() {
    cin >> N;

    printLines(N);

    return 0;
}