#include <iostream>
#include <algorithm>

using namespace std;


int main() {
    int n;
    int x1[100], x2[100];
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> x1[i] >> x2[i];
    }

    int slots[200]{0};
    for (int i{}; i < n; ++i) {
        for (int j{x1[i] + 100}; j < x2[i] + 100; ++j) {
            slots[j] += 1;
        }
    }

    int max = *std::max_element(slots, slots + 200);
    cout << max;


    return 0;
}