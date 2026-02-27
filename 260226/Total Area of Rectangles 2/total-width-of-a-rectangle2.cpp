#include <iostream>
#include <map>

using namespace std;


int main() {
    int N;
    int x1[10], y1[10];
    int x2[10], y2[10];
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];
    }

    std::map<pair<int, int>, bool> seen;
    for (int i{}; i < N; ++i) {
        for (int c{x1[i]}; c < x2[i]; ++c) {
            for (int r{y1[i]}; r < y2[i]; ++r) {
                seen[make_pair(r, c)] = true;  
            }
        }

    }

    cout << seen.size();

    return 0;
}