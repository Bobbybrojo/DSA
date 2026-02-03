#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string str;

int main() {
    cin >> str;

    std::sort(str.begin(), str.end());
    cout << str;

    return 0;
}