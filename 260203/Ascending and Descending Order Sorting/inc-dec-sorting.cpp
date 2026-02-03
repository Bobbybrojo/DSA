#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

int n;
int nums[100];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    std::sort(nums, nums + n);
    for (int i{}; i < n; ++i) {
        std::cout << nums[i] << " ";
    }
    std::cout << '\n';

    std::sort(nums, nums + n, std::greater<int>());
    for (int i{}; i < n; ++i) {
        std::cout << nums[i] << " ";
    }
    std::cout << '\n';

    return 0;
}
