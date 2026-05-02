#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    
    unordered_map<int, int> freq{0};
    
    int n, k;
    cin >> n >> k;
    for (int i{}; i < n; ++i) {
        int num;
        cin >> num;
        freq[num]++;
    }

    vector<pair<int, int>> freq_list(freq.begin(), freq.end());
    sort(freq_list.begin(), freq_list.end(), [](pair<int, int>& p1, pair<int, int>& p2) {
        if (p1.second != p2.second) return p1.second > p2.second;
        return p1.first > p2.first;
    });

    for (int i{}; i < k; ++i) {
        cout << freq_list[i].first << ' ';
    }



    return 0;
}