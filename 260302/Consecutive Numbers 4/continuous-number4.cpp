#include <iostream>

using namespace std;


int main() {
    int N;
    int arr[1000];
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    int last{0};
    int count{0};
    int maxCount{0};
    for (int i{}; i < N; ++i) {
        if (arr[i] > last) {
            count++;
        } else {
            count = 1;
        }

        if (count > maxCount) maxCount = count;
        last = arr[i];
    }

    cout << maxCount;

    return 0;
}