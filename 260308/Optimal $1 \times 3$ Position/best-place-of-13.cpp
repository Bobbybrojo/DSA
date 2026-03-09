#include <iostream>

using namespace std;

int N;
int grid[20][20];

int main() {
    cin >> N;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) cin >> grid[i][j];

    int maxCoins{0};
    for (int r{}; r < N; ++r) {
        for (int i{2}; i < N; ++i) {
            int coins{};
            for (int j{i - 2}; j <= i; ++j) {
                if (grid[r][j] == 1) {
                    coins++;
                }
            }
            maxCoins = max(maxCoins, coins);
        }
    }

    cout << maxCoins;

    return 0;
}