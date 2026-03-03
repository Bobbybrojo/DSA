#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


int main() {
    int n, m;
    char d[1000];
    int t[1000];
    char d2[1000];
    int t2[1000];
    
    cin >> n >> m;

    for (int i = 0; i < n; i++) cin >> d[i] >> t[i];
    for (int i = 0; i < m; i++) cin >> d2[i] >> t2[i];

    std::vector<int> pos1;
    for (int i{}; i < n; ++i) {
        int dir = (d[i] == 'R') ? 1 : -1;
        for (int j{}; j < t[i]; ++j) {
            pos1.push_back((!pos1.empty()) ? pos1.back() + dir : dir);
        }
    }
    std::vector<int> pos2;
    for (int i{}; i < m; ++i) {
        int dir = (d2[i] == 'R') ? 1 : -1;
        for (int j{}; j < t2[i]; ++j) {
            pos2.push_back((!pos2.empty()) ? pos2.back() + dir : dir);
        }
    }

    for (int i{}; i < pos1.size(); ++i) {
        if (pos1[i] == pos2[i]) {
            cout << i + 1;
            return 0;
        }
    }
    cout << -1;

    return 0;
}