#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int n;
int m;
int A[100];

int main() {

    // Recieve inputs
    cin >> n >> m;
    for (int i{}; i < n; ++i) {
        cin >> A[i];
    }

    // DP[i] represents the minimum length of subsequence whose
    //       sum of elements equals i
    // DP[i] = Min( DP[i - A[j]] + 1 ) for all i >= A[j], For all j

    int dp[10000];
    dp[0] = 0;
    for (int i{1}; i <= m; ++i) {
        dp[i] = INT_MAX;
    }

    for (int j{}; j < n; ++j) {
        for (int i{m}; i >= 0; --i) {
            if (i >= A[j] && dp[i - A[j]] != INT_MAX) {
                dp[i] = min(dp[i], dp[i - A[j]] + 1);
            }
        }
    }

    dp[m] != INT_MAX ? cout << dp[m] : cout << -1;  

    return 0;
}