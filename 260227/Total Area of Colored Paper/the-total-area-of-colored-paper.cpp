#include <iostream>
#include <algorithm>
#include <iterator>

using namespace std;


int main() {
    int N;
    int x[100], y[100];
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> x[i] >> y[i];
    }

    int slots[200][200]{0};

    for (int i{}; i < N; ++i) {
        for (int r{y[i] + 100}; r < y[i] + 100 + 8; ++r) {
            for (int c{x[i] + 100}; c < x[i] + 100 + 8; ++c) {
                slots[r][c] = 1;
            }
        }
    }

    int count{};
    for (int r{}; r < 200; ++r) {
        for (int c{}; c < 200; ++c) {
            if (slots[r][c] == 1) count++;
        }
    }
    cout << count;

    return 0;
}