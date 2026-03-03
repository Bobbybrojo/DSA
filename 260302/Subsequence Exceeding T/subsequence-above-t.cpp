#include <iostream>

using namespace std;

int n, t;
int arr[1000];

int main() {
    cin >> n >> t;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int count{};
    int maxCount{};
    for (int i{}; i < n; i++) {
        if (arr[i] > t) {
            count++;
        } else {
            count = 0;
        }

        if (count > maxCount) maxCount = count;
    }

    cout << maxCount;

    return 0;
}