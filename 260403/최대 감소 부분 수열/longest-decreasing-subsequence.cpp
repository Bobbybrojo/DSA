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

    int dp[MAX_N];
    for (int i{}; i < N; ++i) {
        dp[i] = 1;
    }

    for (int i{1}; i < N; ++i) {
        int maxLen{0};
        for (int j{}; j < i; ++j) {
            if (M[j] > M[i]) {
                maxLen = max(maxLen, dp[j]);
            }
        }
        dp[i] = maxLen + 1;
    }

    cout << *max_element(dp, dp + N);


    return 0;
}
