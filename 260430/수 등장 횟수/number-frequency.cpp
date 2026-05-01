#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    
    unordered_map<int, int> freq{0};

    int n, m;
    cin >> n >> m;

    for (int i{}; i < n; ++i) {
        int num;
        cin >> num;
        freq[num] += 1;
    }

    for (int i{}; i < m; ++i) {
        int num;
        cin >> num;
        cout << freq[num] << ' ';
    }

    return 0;
}