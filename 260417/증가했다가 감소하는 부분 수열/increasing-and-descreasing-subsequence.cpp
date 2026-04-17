#include <iostream>
#include <algorithm>

using namespace std;

int n;
int sequence[1000];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> sequence[i];
    }

    int inc[n];
    inc[0] = 1;
    for (int i{1}; i < n; ++i) {
        inc[i] = 1;
        for (int j{}; j < i; ++j) {
            if (sequence[j] < sequence[i])
                inc[i] = max(inc[i], inc[j] + 1);
        }
    }

    int dec[n];
    dec[0] = 1;
    for (int i = n - 1; i >= 0; --i) {
        dec[i] = 1;
        for (int j = i + 1; j < n; ++j) {
            if (sequence[j] < sequence[i])
                dec[i] = max(dec[i], dec[j] + 1);
        }
    }

    int ans = 0;
    for (int i = 0; i < n; ++i)
        ans = max(ans, inc[i] + dec[i] - 1);
    cout << ans;
 
    return 0;
}
