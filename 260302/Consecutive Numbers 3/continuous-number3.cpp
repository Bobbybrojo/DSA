#include <iostream>

using namespace std;

int N;
int arr[1000];

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    int maxCount{0};
    int count{0};
    int positive {true};
    for (int i{}; i < N; ++i) {
        if (positive && arr[i] > 0) {
            count++;
        }
        else if (positive && arr[i] < 0) {
            count = 1;
        }
        else if (!positive && arr[i] > 0) {
            count = 1;
        }
        else if (!positive && arr[i] < 0) {
            count++;
        }

        if (count > maxCount) maxCount = count;

        (arr[i] < 0) ? positive = false : positive = true;
    }

    cout << maxCount;

    return 0;
}