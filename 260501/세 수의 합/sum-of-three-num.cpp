#include <iostream>
#include <unordered_map>

using namespace std;


int main() {

    // Recetrieve inputs
    int n, target;
    cin >> n >> target;

    int nums[1000];
    for (int i{}; i < n; ++i) cin >> nums[i];

    // Solve three sum count
    int answer{};
    for (int i{}; i < n; ++i) {
        int needed = target - nums[i];
        unordered_map<int, int> seen{0};
        for (int j{i + 1}; j < n; ++j) {
            answer += seen[needed - nums[j]];
            seen[nums[j]] += 1;
        }
    }
    cout << answer;

    return 0;
}