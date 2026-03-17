#include <iostream>
#include <algorithm>

using namespace std;

int N;
int grid[20][20];

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> grid[i][j];
        }
    }

    int maxCoinCount{};
    // Pick a top left position row and column
    for (int r{}; r < N - 2; ++r) {
        for (int c{}; c < N - 2; ++c) {

            int coinCount{};
            // Search through 3x3 grid from r, c position at top left
            for (int i{}; i < 3; ++i) {
                for (int j{}; j < 3; ++j) {
                    if (grid[r + i][c + j] == 1){
                        coinCount++;
                    }
                }
            }
            maxCoinCount = std::max(maxCoinCount, coinCount);
        }
    }

    cout << maxCoinCount;

    return 0;
}
