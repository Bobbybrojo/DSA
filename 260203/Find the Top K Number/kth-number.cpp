#include <iostream>
#include <algorithm> 

using namespace std;

int N, k;
int nums[1000];

int main() {
    cin >> N >> k;

    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }

    std::sort(nums, nums + N);
    std::cout << nums[k - 1] << '\n';

    return 0;
}
