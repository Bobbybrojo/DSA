#include <iostream>
#include <algorithm>

using namespace std;

int n;
int arr[100];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];

        if ((i + 1) % 2 == 1) {
            sort(arr, arr + i + 1);
            cout << arr[i / 2] << ' ';
        }
    }

    // Please write your code here.

    return 0;
}