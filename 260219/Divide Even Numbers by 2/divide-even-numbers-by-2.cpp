#include <iostream>

using namespace std;

void divideEvens(int arr[], int size) {
    for (int i{}; i < size; ++i) {
        if (arr[i] % 2 == 0) {
            arr[i] = arr[i] / 2;
        }
    }
}


int main() {
    int n;
    int arr[50];
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    divideEvens(arr, n);

    for (int i{}; i < n; ++i) {
        cout << arr[i] << ' ';
    }

    return 0;
}