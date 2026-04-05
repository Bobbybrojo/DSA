#include <iostream>
#include <algorithm>

using namespace std;

int n;
int m;
int arr[50][50];

int main() {
    cin >> n;
    cin >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }

    // DP[r][c] represents the max # of cells stepped on while
    //          following the specific rules to reach (r, c)
    // DP[r][c] = max of all DP[r - N][c - M] where
    //            arr[r-N][c - M] < arr[r][c] for all N, M >= 1

    int dp[50][50];
    dp[0][0] = 1;
    for (int i{1}; i < n; ++i) dp[i][0] = -1;
    for (int i{1}; i < m; ++i) dp[0][i] = -1;

    for (int r{1}; r < n; ++r) {
        for (int c{1}; c < n; ++c) {
            int maxCells = -1;
            for (int j{1}; r - j >= 0; ++j) {
                for (int k{1}; c - k >= 0; ++k) {
                    if (dp[r - j][c - k] != -1 && arr[r - j][c - k] < arr[r][c]) {
                        maxCells = max(maxCells, dp[r - j][c - k] + 1);
                    }
                }
            }
            dp[r][c] = maxCells;
        }
    }

    int ans{-1};
    for (int r{}; r < n; ++r) {
        for (int c{}; c < m; ++c) {
            if (dp[r][c] != -1) {
                ans = max(ans, dp[r][c]);
            }
        }
    }

    cout << ans;


    return 0;
}
