#include <iostream>
#include <algorithm>

using namespace std;


int main() {
    int N;
    int arr[1000];
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    int count{};
    int max_count{0};
    int last;
    for (int i{0}; i < N; ++i) {
        if (i == 0) {
            count++;
        }
        else if (last == arr[i]) {
            count++;
        } else {
            count = 0;
        }
        max_count = max(max_count, count + 1);
        last = arr[i];
    }

    cout << max_count;

    return 0;
}