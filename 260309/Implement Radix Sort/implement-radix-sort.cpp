#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int n;
int arr[100000];

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Find K
    int k{};
    for (int i{}; i < n; ++i) {
        k = std::max(k, (int)std::to_string(arr[i]).size());
    }


    // Perform radix sort
    for (int pos{k - 1}; pos >= 0; --pos) {
        std::vector<int> newArr[10];
        for (int i{}; i < n; ++i) {
            string s = std::to_string(arr[i]);
            int charIdx = pos - (k - (int)s.size());
            if (charIdx < 0) {
                newArr[0].push_back(arr[i]);
            } else {
                newArr[s[charIdx] - '0'].push_back(arr[i]);
            }
        }

        std::vector<int> storeArr;
        for (int i{}; i < 10; ++i) {
            for (int j{}; j < newArr[i].size(); j++) {
                storeArr.push_back(newArr[i][j]);
            }
        }

        std::copy(storeArr.begin(), storeArr.end(), arr);
    }

    // Print result
    for (int i{}; i < n; ++i) {
        cout << arr[i] << ' ';
    }
    
    return 0;
}
