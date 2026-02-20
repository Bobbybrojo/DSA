#include <iostream>
#include <string>

using namespace std;

bool isPalindrome(string &s) {
    int n = s.size();
    for (int i{}; i < n / 2; ++i) {
        if (s[i] != s[n - 1 - i]) return false;
    }
    return true;
}

int main() {
    string A;
    cin >> A;

    isPalindrome(A) ? cout << "Yes" : cout << "No";

    return 0;
}