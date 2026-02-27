#include <iostream>
#include <unordered_map>
#include<vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> x(n);
    vector<char> dir(n);
    for (int i = 0; i < n; i++) {
        cin >> x[i] >> dir[i];
    }

    // Track (whiteCount, blackCount) for each position
    unordered_map<int, tuple<int, int, int>> tiles;  // position -> {whiteCount, blackCount}
    int position = 0;
    
    for (int i = 0; i < n; ++i) {
        int amount = x[i];
        char direction = dir[i];

        if (direction == 'L') {
            for (int j = position; j > position - amount; --j) {  // ✓ Correct bound
                auto& [wc, bc, last] = tiles[j];
                wc++;
                last = 1;
            }
            position -= amount - 1;
        } else {
            for (int j = position; j < position + amount; ++j) {  // ✓ Correct bound
                auto& [wc, bc, last] = tiles[j];
                bc++;
                last = 2;
            }
            position += amount - 1;
        }
    }

    int w = 0, b = 0, g = 0;
    for (auto& [k, v] : tiles) {
        auto& [wc, bc, last] = v;
        if (wc >= 2 && bc >= 2) {
            g++;
        } else if (last == 1) {
            w++;  // More white (last painted white)
        } else if (last == 2) {
            b++;  // More black (last painted black)
        }
    }

    cout << w << ' ' << b << ' ' << g;
    return 0;
}