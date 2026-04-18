#include <iostream>
#include <tuple>
#include <algorithm>
using namespace std;

int n;
//   start, end, price
tuple<int, int, int> jobs[1000];

bool overlapping(tuple<int, int, int>& j1, tuple<int, int, int>& j2) {
    return !(get<1>(j1) < get<0>(j2) || get<1>(j2) < get<0>(j1));
}

int main() {

    // Consume inputs
    cin >> n;
    for (int i{}; i < n; ++i) {
        int s, e, p;
        cin >> s >> e >> p;
        jobs[i] = {s, e, p};
    }

    // DP[i] represents the maximized total earnings of jobs selected through job i
    // DP[i] = max(DP[j] + job[i].price) for all j < i if job[i] not overlapping job[j]

    int dp[1000];
    dp[0] = get<2>(jobs[0]);

    for (int i{1}; i < n; ++i) {
        dp[i] = get<2>(jobs[i]);
        for (int j{}; j < i; ++j) {
            if (!overlapping(jobs[i], jobs[j])) {
                dp[i] = max(dp[i], dp[j] + get<2>(jobs[i]));
            }
        }
    }

    // Print answer
    cout << *max_element(dp, dp + n);


    return 0;
}