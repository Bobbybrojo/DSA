#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;


int main() {
    int n;
    int nums[100];
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    std::sort(nums, nums + n);
    for (int i{}; i < n; ++i) {
        cout << nums[i] << ' ';
    }
    cout << '\n';

    std::sort(nums, nums + n, std::greater<int>());
    for (int i{}; i < n; ++i) {
        cout << nums[i] << ' ';
    }

    return 0;
}
