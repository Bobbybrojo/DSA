#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int n;
int m;
int coins[100];

int main() {
    
    cin >> n >> m;
    for (int i{}; i < n; ++i) {
        cin >> coins[i];
    }

    // Sort coins
    sort(coins, coins + n);

    // DP[i] represents the minimum number of coins needed to make value i
    // DP[i] = DP[j] + 1 for all j < i if coins contains C where j + C = i

    int dp[10001];
    dp[0] = 0;
    for (int i{1}; i <= m; ++i) {
        dp[i] = -1;
    }

    for (int i{1}; i <= m; ++i) {
        dp[i] = INT_MAX;

        for (int c{}; c < n; ++c) {
            int j = i - coins[c];

            if (coins[c] > i) break;

            if (dp[j] != -1) {
                dp[i] = min(dp[i], dp[j] + 1);
            }    
        }

        if (dp[i] == INT_MAX) dp[i] = -1;
    }

    int ans = dp[m] != INT_MAX ? dp[m] : -1;
    cout << ans;

    

    return 0;
}