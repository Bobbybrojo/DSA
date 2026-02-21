#include <iostream>
#include <map>

using namespace std;

bool sameElements(int* l1, int* l2, int size) {
    std::map<int, int> freq1{};
    for (int i{}; i < size; ++i) {
        freq1[l1[i]] += 1;
    }

    std::map<int, int> freq2{};
    for (int i{}; i < size; ++i) {
        freq2[l2[i]] += 1;
    }

    return freq1 == freq2;
}

int main() {
    int n;
    int A[100];
    int B[100];
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    for (int i = 0; i < n; i++) {
        cin >> B[i];
    }

    sameElements(A, B, n) 
    ? cout << "Yes" 
    : cout << "No";

    
    return 0;
}