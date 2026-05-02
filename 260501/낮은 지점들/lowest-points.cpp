#include <iostream>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main() {
    
    int n;
    cin >> n;

    unordered_map<int, int> lowPoints;
    for (int i{}; i < n; ++i) {
        int x, y;
        cin >> x >> y;

        if (lowPoints.find(x) != lowPoints.end()) {
            lowPoints[x] = min(lowPoints[x], y);
        } else {
            lowPoints[x] = y;
        }
    }

    long long sum{};
    for (auto [x, y] : lowPoints) {
        sum += y;
    }
    cout << sum;

    return 0;
}