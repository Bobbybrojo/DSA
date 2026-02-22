#include <iostream>
#include <algorithm>

using namespace std;

int N, K;
int A[100], B[100];

int main() {
    cin >> N >> K;

    for (int i = 0; i < K; i++) {
        cin >> A[i] >> B[i];
    }

    int slots[N]{0};
    for (int i{}; i < K; ++i) {
        for (int j{A[i]}; j <= B[i]; ++j) {
            slots[j] += 1;
        }
    }

    cout << *std::max_element(slots, slots + N);



    return 0;
}