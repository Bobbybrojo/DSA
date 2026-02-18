#include <iostream>

using namespace std;

bool isContiguousSubsequence(int a[], int sizeA, int b[], int sizeB) {
    for (int i{}; i < sizeA; ) {
        if (a[i] == b[0]) {
            int j { 0 };
            while (a[i] == b[j]) {
                ++i;
                ++j;
            }
            if (j == sizeB) {
                return true;
            } else {
                ++i;
            }
        } else {
            ++i;
        }
    }
    return false;
}

int main() {
    int n1, n2;
    int a[100], b[100];

    cin >> n1 >> n2;

    for (int i = 0; i < n1; i++) cin >> a[i];

    for (int i = 0; i < n2; i++) cin >> b[i];

    const char* res = (isContiguousSubsequence(a, n1, b, n2)) ? "Yes" : "No";

    cout << res;

    return 0;
}