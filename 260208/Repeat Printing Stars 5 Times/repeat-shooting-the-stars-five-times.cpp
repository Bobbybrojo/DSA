#include <iostream>
using namespace std;

void printStars() {
    cout << "**********" << '\n';
}

int main() {
    
    for (int i{}; i < 5; ++i) {
        printStars();
    }
    

    return 0;
}