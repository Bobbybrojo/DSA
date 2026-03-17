#include <iostream>

using namespace std;

int n, m;
int grid[100][100];

int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    int happySequences{};

    // Count happy sequences within each row sequence
    for (int r{}; r < n; ++r) {
        int prev{grid[r][0]};
        int seqLen{1};

        if (seqLen >= m) {
            happySequences++;
            continue;
        }

        for (int i{1}; i < n; ++i) {

            if (grid[r][i] == prev) {
                seqLen += 1;
                if (seqLen >= m) {
                    happySequences++;
                    break;
                }
            } else {
                prev = grid[r][i];
                seqLen = 1;
            }
        }
    }

    // Count happy sequences within each column sequence
    for (int c{}; c < n; ++c) {
        int prev{grid[0][c]};
        int seqLen{1};

        if (seqLen >= m) {
            happySequences++;
            continue;
        }

        for (int i{1}; i < n; ++i) {
            if (grid[i][c] == prev) {
                seqLen += 1;
                if (seqLen >= m) {
                    happySequences++;
                    break;
                }
            } else {
                prev = grid[i][c];
                seqLen = 1;
            }
        }
    }

    cout << happySequences;

    return 0;
}
