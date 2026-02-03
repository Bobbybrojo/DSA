#include <iostream>
#include <algorithm>

using namespace std;

int N;
int nums[2000];

int main() {
    cin >> N;

    for (int i = 0; i < 2 * N; i++) {
        cin >> nums[i];
    }

    std::sort(nums, nums + 2 * N);

    int maxSum = 0;
    for (int i{}; i < 2 * N; ++i) {
        int sum = nums[i] + nums[2 * N - 1 - i];
        if (sum > maxSum) {
            maxSum = sum;
        }
    }
    std::cout << maxSum << '\n';
    

    return 0;
}
