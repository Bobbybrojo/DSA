#include <iostream>
#include <unordered_map>

using namespace std;


int main() {
    int n;
    int x[100];
    char dir[100];
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> x[i] >> dir[i];
    }

    int total{};
    std::unordered_map<int, int> seen{0};
    int position = 0;

    for (int i{}; i < n; ++i) {
        int amt = x[i];


        if (dir[i] == 'L') {
            for (int j{position - 1}; j >= position - amt; --j) {
                seen[j]++;
            }
            position -= amt;
        } else {
            for (int j{position + 1}; j <= position + amt; ++j) {
                seen[j]++;
            }
            position += amt;
        }
    }


    for (auto& [pos, amt] : seen) {
        if (amt >= 2) total += 1;
    }
    
    cout << total;

    return 0;
}