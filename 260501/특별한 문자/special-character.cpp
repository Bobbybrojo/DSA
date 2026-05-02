#include <iostream>
#include <map>
using namespace std;

int main() {
    string str;
    cin >> str;

    map<char, int> freq;
    for (char c: str) freq[c] += 1;

    for (char c: str) {
        if (freq[c] == 1) {
            cout << c;
            return 0;
        }
    }

    cout << "None";

    return 0;
}