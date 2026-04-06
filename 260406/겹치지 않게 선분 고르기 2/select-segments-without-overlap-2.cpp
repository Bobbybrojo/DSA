#include <iostream>
#include <algorithm>
#include <utility>

using namespace std;

int n;
int x1[1000];
int x2[1000];

bool isOverlapping(int x1, int x2, int y1, int y2) {
    return !(x2 < y1 || y2 < x1);
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x1[i] >> x2[i];
    }

    // Sort the segments by starting point
    pair<int,int> segs[1000];
    for (int i{}; i < n; ++i) segs[i] = {x1[i], x2[i]};
    sort(segs, segs + n);
    for (int i{}; i < n; ++i) {
        x1[i] = segs[i].first;
        x2[i] = segs[i].second;
    }

    // DP[i] represents the maximum number of non-overlapping segments that
    //       can be selected ending with segment i
    // DP[i] = max(DP[j] + 1 for all j < i where DP[j] != -1 and DP[j] is not overlapping DP[i])

    // Initialize dp
    int dp[1000];
    dp[0] = 1;
    for (int i{1}; i < n; ++i) {
        dp[i] = -1;
    }

    // Perform Recurrence
    for (int i{1}; i < n; ++i) {
        int maxNum{1};
        for (int j{}; j < i; ++j) {
            if (dp[j] != -1 && !isOverlapping(x1[i], x2[i], x1[j], x2[j])) {
                maxNum = max(maxNum, dp[j] + 1);
            }
        }
        dp[i] = maxNum;
    }

    cout << *max_element(dp, dp + n);

    return 0;
}
