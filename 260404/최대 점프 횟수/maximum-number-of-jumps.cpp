#include <iostream>
#include <algorithm>

using namespace std;

const int MAX_N = 1000;

int N;
int M[MAX_N];

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> M[i];
    }

    // DP[i] represents the maximum number of jumps made to get to position i
    // DP[i] = max(DP[i - n] for all n where i - n >= 0 and n < i)

    int dp[MAX_N];
    dp[0] = 0;
    for (int i{1}; i < N; ++i) {
        dp[i] = -1;
    }

    for (int i{1}; i < N; ++i) {
        int maxJumps{-1};
        for (int j{0}; j < i; j++) {
            if (j + M[j] >= i && dp[j] != -1) {
                maxJumps = max(maxJumps, dp[j] + 1);
            }
        }
        dp[i] = maxJumps;
    }

    int ans{};
    for (int i{}; i < N; ++i) {
        if (dp[i] != -1) ans = max(ans, dp[i]);
    }

    cout << ans;

    return 0;
}
