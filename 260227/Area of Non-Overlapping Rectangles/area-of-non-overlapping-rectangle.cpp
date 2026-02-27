#include <iostream>

using namespace std;

int main() {
    int x1[3], y1[3];
    int x2[3], y2[3];
    cin >> x1[0] >> y1[0] >> x2[0] >> y2[0];
    cin >> x1[1] >> y1[1] >> x2[1] >> y2[1];
    cin >> x1[2] >> y1[2] >> x2[2] >> y2[2];

    int points[2000][2000]{0};
    for (int i{}; i < 3; ++i) {
        int sr = y1[i] + 1000, er = y2[i] + 1000;
        int sc = x1[i] + 1000, ec = x2[i] + 1000;
        for (int r{sr}; r < er; ++r) {
            for (int c{sc}; c < ec; ++c) {
                points[r][c] = 1;
                if (i == 3 - 1) points[r][c] = 0;
            }
        }
    }

    int count{};
    for (int r{}; r < 2000; ++r) {
        for (int c{}; c < 2000; ++c) {
            if (points[r][c] == 1) count++;
        }
    }

    cout << count;

    return 0;
}