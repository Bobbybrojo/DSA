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
    std::unordered_map<int, int> seen; // 0=unvisited, 1=right only, 2=left only, 3=both
    int position = 0;

    for (int i{}; i < n; ++i) {
        int amt = x[i];


        if (dir[i] == 'L') {
            for (int j{position}; j > position - amt; --j) {
                if (seen[j] == 1)
                    seen[j] = 3;
                else if (seen[j] != 3) 
                    seen[j] = 2;   
            }
            position -= amt;
        } else {
            for (int j{position}; j < position + amt; ++j) {
                if (seen[j] == 2)
                    seen[j] = 3;
                else if (seen[j] != 3) 
                    seen[j] = 1;
            }
            position += amt;
        }
    }


    for (auto& [pos, amt] : seen) {
        if (amt == 3) total++;
    }
    
    cout << total + 1;

    return 0;
}