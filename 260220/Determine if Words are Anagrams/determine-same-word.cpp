#include <iostream>
#include <string>
#include <algorithm>

using namespace std;


int main() {
    string word1;
    string word2;
    cin >> word1;
    cin >> word2;

    sort(word1.begin(), word1.end());
    sort(word2.begin(), word2.end());

    word1 == word2 ? cout << "Yes" : cout << "No";

    return 0;
}
