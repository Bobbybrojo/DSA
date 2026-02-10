#include <iostream>

using namespace std;

bool isWhole(int x) {
    return !(x % 2 == 0 || x % 10 == 5 || (x % 3 == 0 && x % 9 != 0));
}

int main() {
    int a, b;
    cin >> a >> b;

    int count{};
    for (int i{a}; i <= b; ++i)
        if (isWhole(i)) 
            count++;
    
    cout << count;

    return 0;
}