#include <iostream>
#include <algorithm>

using namespace std;

void minimum(int a, int b, int c) {
    cout << min(a, min(b, c));
}

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    minimum(a, b, c);

    return 0;
}