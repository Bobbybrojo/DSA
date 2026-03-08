#include <iostream>
#include <algorithm>

using namespace std;

int n;
int A[100];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    int travelDistances[n]{};

    for (int i{}; i < n; ++i) {
        for (int j{}; j < n; ++j) {
            if (j != i) {
                travelDistances[i] += A[j] * (std::max(i, j) - std::min(i, j));
            }
        }
    }

    cout << *std::min_element(travelDistances, travelDistances + n);

    return 0;
}