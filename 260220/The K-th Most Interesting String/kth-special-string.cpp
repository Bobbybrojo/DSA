#include <iostream>
#include <string>
#include <algorithm>

using namespace std;


int main() {
    int n, k;
    string t;
    string str[100];
    cin >> n >> k >> t;

    for (int i = 0; i < n; i++) {
        cin >> str[i];
    }

    sort(str, str + n);
    int lo = 0;
    int hi = n - 1;
    int mid;
    while (lo <= hi) {
        mid = lo + (hi - lo) / 2;
        string s = str[mid];
        if (s < t) {
            lo = mid + 1;
            if (str[lo].find(t) == 0) {
                break;
            }
        }
        else if (s >= t) {
            hi = mid - 1;
        }
    }

    cout << str[lo + k - 1];


    return 0;
}