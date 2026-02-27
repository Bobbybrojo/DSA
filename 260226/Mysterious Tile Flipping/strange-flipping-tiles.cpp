#include <iostream>
#include <unordered_map>

using namespace std;

int n;
int x[1000];
char dir[1000];

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> x[i] >> dir[i];
    }

    int position{0};
    std::unordered_map<int, int> tiles{0};  
    for (int i{}; i < n; ++i) {
        int amount {x[i]};
        char direction {dir[i]};

        if (direction == 'R') {
            for (int j{position}; j < position + amount; j++) {
                tiles[j] = 1;
            }
            position += amount - 1;
        } else {
            for (int j {position}; j > position - amount; --j) {
                tiles[j] = 2;
            }
            position -= amount - 1;
        }
    }

    int w{};
    int b{};
    for (const auto& [_p, c] : tiles) {
        if (c == 1) b++;
        if (c == 2) w++;
    }

    cout << w << ' ' << b;

    return 0;
}