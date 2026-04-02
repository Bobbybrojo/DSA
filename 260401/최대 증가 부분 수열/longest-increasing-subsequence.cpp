#include <iostream>
#include <algorithm>

using namespace std;

int N;
int M[1000];

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> M[i];
    }

    // DP[i] represents the length of the longest increasing subsequence ending on index i from the given numbers
    // dp[i] = max(dp[j] + 1)  for all j < i where M[j] < M[i]
    // dp[i] = 1               if no such j exists (the element alone is a subsequence of length 1) 

    int dp[N + 1];
    for (int i{}; i <= N; ++i) {
        dp[i] = 1;
    }

    for (int i{1}; i <= N; ++i) {
        int maxLen{}; 
        for (int j{}; j < i; ++j) {
            if (M[i] > M[j]) {
                maxLen = max(maxLen, dp[j]);
            }
        }
        dp[i] = maxLen + 1;
    }

    cout << *max_element(dp, dp + N + 1);

    return 0;
}
