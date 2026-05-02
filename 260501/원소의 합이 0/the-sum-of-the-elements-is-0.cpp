#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    int A[5000];
    int B[5000];
    int C[5000];
    int D[5000];

    int n;
    cin >> n;
    for (int i{}; i < n; ++i) cin >> A[i];
    for (int i{}; i < n; ++i) cin >> B[i];
    for (int i{}; i < n; ++i) cin >> C[i];
    for (int i{}; i < n; ++i) cin >> D[i];

    // A + B = -(C + D)

    unordered_map<int, int> ABSums{};
    for (int i{}; i < n; ++i) {
        for (int j{}; j < n; ++j) {
            ABSums[A[i] + B[j]] += 1;
        }
    }

    int answer{};
    for (int i{}; i < n; ++i) {
        for (int j{}; j < n; ++j) {
            answer += ABSums[-(C[i] + D[j])];
        }
    }

    cout << answer;

    return 0;
}