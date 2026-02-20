#include <iostream>
#include <string>
#include <algorithm>

using namespace std;


int main() {
    int n;
    string word[100];
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> word[i];
    }

    std::sort(word, word + n);
    for (int i{}; i < n; ++i) {
        cout << word[i] << '\n';
    }

    return 0;
}