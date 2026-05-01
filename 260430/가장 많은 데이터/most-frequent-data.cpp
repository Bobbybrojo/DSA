#include <iostream>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main() {

    unordered_map<string, int> string_freq{0};

    int n;
    cin >> n;
    for (int i{}; i < n; ++i) {
        string s;
        cin >> s;
        string_freq[s] += 1;
    }

    int max_freq{};
    for (auto [s, f] : string_freq) {
        max_freq = max(max_freq, f);
    }
    cout << max_freq;

    return 0;
}