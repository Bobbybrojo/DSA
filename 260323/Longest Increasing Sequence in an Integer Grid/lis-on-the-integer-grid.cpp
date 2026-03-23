#include <iostream>
#include <algorithm>
#include <tuple>
#include <vector>

#define MAX_N 500

using namespace std;

bool in_range(int r, int c, int n) {
    return r >= 0 && r < n && c >= 0 && c < n;
}

int main() {
    int n;
    int grid[100][100];
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    // Sort the positions of cells in ascending order
    vector<tuple<int, int, int>> cells;
    for (int r{}; r < n; ++r)
        for (int c{}; c < n; ++c)
            cells.push_back(make_tuple(grid[r][c], r, c));

    sort(cells.begin(), cells.end());

    // Initialize dp table
    int dp[MAX_N][MAX_N];
    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < n; ++c) {
            dp[r][c] = 1;
        }
    }

    int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    // Start from smallest value cell and update dp values for 4 dirs
    for (int i{}; i < (int)cells.size(); ++i) {
        auto [val, r, c] = cells[i];

        for (auto [dr, dc] : directions) {
            int nr = r + dr, nc = c + dc;

            if (in_range(nr, nc, n) && grid[nr][nc] > val) {
                dp[nr][nc] = max(dp[nr][nc], dp[r][c] + 1);
            }
        }
    }

    // Find max among dp table
    int ans{};
    for (int r{}; r < n; ++r) {
        for (int c{}; c < n; ++c) {
            ans = max(ans, dp[r][c]);
        }
    }

    cout << ans;  

    return 0;
}
