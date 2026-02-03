#include <iostream>
#include <algorithm>

using namespace std;

int n;
int A[100];
int B[100];

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    for (int i = 0; i < n; i++) {
        cin >> B[i];
    }

    std::sort(A, A + n);
    std::sort(B, B + n);
    for (int i{}; i < n; ++i) {
        if (A[i] != B[i]) {
            std::cout << "No" << '\n';
            return 0;
        }
    }
    std::cout << "Yes" << '\n';

    return 0;
}