#include <iostream>
#include <vector>

using namespace std;

int N, M;
int v[1000], t[1000];
int v2[1000], t2[1000];

int main() {
    cin >> N >> M;

    for (int i = 0; i < N; i++) cin >> v[i] >> t[i];

    for (int i = 0; i < M; i++) cin >> v2[i] >> t2[i];

    int currPos1{0};
    std::vector<int> pos1;
    for (int i{}; i < N; ++i) {
        for (int j{}; j < t[i]; ++j) {
            currPos1 += v[i];
            pos1.push_back(currPos1);
        }
    }

    int currPos2{0};
    std::vector<int> pos2;
    for (int i{}; i < M; ++i) {
        for (int j{}; j < t2[i]; ++j) {
            currPos2 += v2[i];
            pos2.push_back(currPos2);
        }
    }

    int leading = 0;
    int changes{-1};
    for (int i{}; i < pos1.size(); ++i) {
        int leadingBefore = leading;
        if (pos1[i] > pos2[i]) {
            leading = 1;
        } 
        else if (pos2[i] > pos1[i]) {
            leading = 2;
        }

        if (leadingBefore != leading) {
            changes++;
        }
    }

    cout << changes;

    return 0;
}