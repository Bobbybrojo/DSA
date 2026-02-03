#include <iostream>
#include <string>
#include <string_view>
#include <algorithm>

using namespace std;

int n, k;
string t;
string str[100];

int main() {
    cin >> n >> k >> t;

    for (int i = 0; i < n; i++) {
        cin >> str[i];
    }

    sort(str, str + n);
    for (int i{}; i < n; ++i) {
        if (string_view(str[i]).substr(0, t.size()) == t) {
            std::cout << str[i + k - 1] << '\n';
            return 0;
        }
    }


    return 0;
}