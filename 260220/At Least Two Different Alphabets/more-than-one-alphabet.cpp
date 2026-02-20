#include <iostream>
#include <string>

using namespace std;

bool twoAlphabets(string& s) {
    for (int i{1}; i < s.size(); ++i) {
        if (s[i] != s[0]) {
            return true;
        }
    }
    return false;
}

int main() {
    string A;
    cin >> A;

    twoAlphabets(A) ? cout << "Yes" : cout << "No";

    return 0;
}