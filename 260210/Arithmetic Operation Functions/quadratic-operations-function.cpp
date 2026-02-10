#include <iostream>

using namespace std;

int add(int a, int b) {
    return a + b;
}

int sub(int a, int b) {
    return a - b;
}

int mul(int a, int b) {
    return a * b;
}

int divide(int a, int b) {
    return a / b;
}

int main() {
    int a;
    int c;
    char o;
    cin >> a >> o >> c;

    switch (o) {
        case '+':
            cout << a << ' ' << o << ' ' << c << " = " << add(a, c);
            break;
        case '-':
            cout << a << ' ' << o << ' ' << c << " = " << sub(a, c);
            break;
        case '*':
            cout << a << ' ' << o << ' ' << c << " = " << mul(a, c);
            break;
        case '/':
            cout << a << ' ' << o << ' ' << c << " = " << divide(a, c);
            break;
        default:
            cout << "False";
            break;
    }

    return 0;
}