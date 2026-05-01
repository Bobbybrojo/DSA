#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <cctype>
using namespace std;

int main() {
    
    unordered_map<string, int> s_to_i{};
    unordered_map<int, string> i_to_s{};

    int n, m;
    cin >> n >> m;
    for (int i{1}; i <= n; ++i) {
        string s;
        cin >> s;

        s_to_i[s] = i;
        i_to_s[i] = s;
    }

    for (int i{}; i < m; ++i) {
        string query;
        cin >> query;

        if (all_of(query.begin(), query.end(), [](unsigned char c) {
            return isdigit(c);
        })) {
            cout << i_to_s[atoi(query.c_str())] << '\n';
        }
        else {
            cout << s_to_i[query] << '\n';
        }
    }

    return 0;
}