#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    
    int n;
    cin >> n;
    
    string words[1000];
    for (int i{}; i < n; ++i) cin >> words[i];
    
    vector<unordered_map<char, int>> all_frequencies;

    for (int i{}; i < n; ++i) {
        unordered_map<char, int> freq{0};
        for (char c : words[i]) {
            freq[c] += 1;
        }
        all_frequencies.push_back(freq);
    }

    int maxCount{};
    for (int i{}; i < n; ++i) {
        int count{1};
        for (int j{i + 1}; j < n; ++j) {
            if (all_frequencies[i] == all_frequencies[j]) {
                count++;
            }
        }
        maxCount = max(maxCount, count);
    }
    
    cout << maxCount;

    return 0;
}