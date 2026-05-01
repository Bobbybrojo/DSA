#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    
    // Maps number to the number's frequency
    unordered_map<int, int> seen{0};
    int n, target;
    cin >> n >> target;

    int answer{};
    for (int i{}; i < n; ++i) {
        int num;
        cin >> num;
        answer += seen[target - num];
        seen[num]++;
    }

    cout << answer;

    return 0;
}