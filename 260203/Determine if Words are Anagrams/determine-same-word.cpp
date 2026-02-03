#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string word1;
string word2;

int main() {
    cin >> word1;
    cin >> word2;

    std::sort(word1.begin(), word1.end());
    std::sort(word2.begin(), word2.end());

    if (word1 != word2) {
        std::cout << "No" << std::endl;
        return 0;
    }
    std::cout << "Yes\n";

    return 0;
}
