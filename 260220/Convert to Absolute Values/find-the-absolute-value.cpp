#include <iostream>

using namespace std;

void absoluteList(int (&list)[50], int& size) {
    for (int i{}; i < size; ++i) {
        list[i] = abs(list[i]);
    }
}

int main() {
    int n;
    int arr[50];
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    absoluteList(arr, n);

    for (int i{}; i < n; ++i) {
        cout << arr[i] << ' ';
    }

    return 0;
}