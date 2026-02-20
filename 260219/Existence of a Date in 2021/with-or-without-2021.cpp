#include <iostream>

using namespace std;

bool dateIn2021(int m, int d) {
    if (!(m <= 12 && m >= 1 && d >= 1 && d <= 31)) return false;

    switch (m) {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            return d <= 31;
            break;
        case 2:
            return d <= 28;
            break;
        default:
            return d <= 30;
    }
}


int main() {
    int M, D;
    cin >> M >> D;

    const char* res = dateIn2021(M, D) ? "Yes" : "No";
    cout << res;

    return 0;
}