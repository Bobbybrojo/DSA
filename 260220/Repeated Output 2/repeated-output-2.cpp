#include <iostream>

using namespace std;

void repeatOutput(int n) {
    if (n == 0) {
        return;
    }
    
    cout << "HelloWorld" << '\n';
    repeatOutput(n - 1);
}

int main() {
    int N;
    cin >> N;

    repeatOutput(N);


    return 0;
}