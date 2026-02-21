#include <iostream>
#include <algorithm>

using namespace std;


int main() {
    int N;
    int nums[2000];
    cin >> N;

    for (int i = 0; i < 2 * N; i++) {
        cin >> nums[i];
    }

    sort(nums, nums + 2 * N);
    int maxSum{};
    for (int i{}; i <= N; ++i) {
        maxSum = max(maxSum, nums[i] + nums[2 * N - 1 - i]);
    }

    cout << maxSum;

    return 0;
}
