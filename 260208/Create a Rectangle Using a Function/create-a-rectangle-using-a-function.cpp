#include <iostream>

using namespace std;

int n, m;

void printRectangle(int n, int m) {
    for (int i{}; i < n; ++i) {
        for (int j{}; j < m; ++j) {
            cout << "1";
        }
        cout << '\n';
    }
}

int main() {
    cin >> n >> m;

    printRectangle(n, m);

    return 0;
}