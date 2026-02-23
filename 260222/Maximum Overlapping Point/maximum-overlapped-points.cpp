#include <iostream>
#include <algorithm>

using namespace std;

int n;
int x1[100], x2[100];

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> x1[i] >> x2[i];
    }

    int slots[101]{0};

    for (int i{}; i < n; i++) {
        for (int j{x1[i]}; j <= x2[i]; ++j) {

            slots[j] += 1;

        }
    }

    cout << *std::max_element(slots, slots + 101);



    return 0;
}