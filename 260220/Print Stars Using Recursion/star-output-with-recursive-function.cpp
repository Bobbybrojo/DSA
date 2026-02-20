#include <iostream>

using namespace std;

void printStars(int n, int curr) {
    for (int i{0}; i < curr; ++i) {
        cout << '*';
    }
    cout << '\n';
    
    if (curr == n) return;
    
    printStars(n, curr + 1);

}

int main() {
    int n;
    cin >> n;

    printStars(n, 1);

    return 0;
}