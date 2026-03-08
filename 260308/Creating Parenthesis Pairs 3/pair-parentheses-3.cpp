#include <iostream>
#include <string>

using namespace std;

string A;

int main() {
    cin >> A;

    int count{};
    for (int i{}; i < A.size(); ++i) {
        if (A[i] != '(') continue;

        for (int j{i + 1}; j < A.size(); j++) {
            if (A[j] == ')') count++;
        }
    }

    cout << count;

    return 0;
}