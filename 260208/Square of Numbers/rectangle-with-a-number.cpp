#include <iostream>

using namespace std;

int N;

void squareOfNumbers(int n) {
    int count = 1;

    for (int i{}; i < n; ++i) {
        for (int j{}; j < n; ++j) {
            cout << count << ' ';
            count++;
            if (count >= 10) {
                count = count % 10 + 1;
            }
        }
        cout << '\n';
    }
}

int main() {
    cin >> N;

    squareOfNumbers(N);

    return 0;
}