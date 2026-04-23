#include <iostream>
#include <algorithm>

using namespace std;

int n;
int arr[3] = {1, 2, 5};

int main() {
    cin >> n;

    // DP[i] represents the number of ways to express integer i as a sum of 1, 2, and 5
    // DP[i] = sum(dp[i - arr[j]]) where i - arr[j] >= 0 and 0 <= j <= 2

    int dp[1001];
    dp[0] = 1;
    for (int i{1}; i <= n; ++i) {
        dp[i] = 0;
    }

    for (int i{0}; i <= n; ++i) {
        for (int j{}; j < 3; ++j) {
            if (i - arr[j] >= 0) {
                dp[i] = (dp[i] + dp[i - arr[j]]) % 10007;
            }
        }
    }

    cout << dp[n];


    return 0;
}