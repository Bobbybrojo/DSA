#include <iostream>
#include <algorithm>

using namespace std;

int n;
int grid[100][100];
int dp[100][100];

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    // DP[r][c] represents the minimized maximum value
    // along the path traversed
    // DP[r][c] = Max(grid[r][c], Min(DP[r - 1][c], DP[r][c - 1]))

    // Initialize dp table
    dp[0][0] = grid[0][0];
    for (int i{1}; i < n; ++i) {
        dp[0][i] = max(grid[0][i], grid[0][i - 1]);
        dp[i][0] = max(grid[i][0], grid[i - 1][0]);
    }

    // Fill dp table by tabulation
    for (int r{}; r < n; ++r) {
        for (int c{}; c < n; ++c) {
            dp[r][c] = max(grid[r][c], min(dp[r - 1][c], dp[r][c-1]));
        }
    }

    cout << dp[n - 1][n - 1];

    return 0;
}
