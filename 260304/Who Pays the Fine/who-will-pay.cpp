#include <iostream>

using namespace std;

int N, M, K;
int student[10000];

int main() {
    cin >> N >> M >> K;

    for (int i = 0; i < M; i++) {
        cin >> student[i];
    }

    int studentFines[N + 1]{0};
    for (int i{}; i < M; ++i) {
        studentFines[student[i]] += 1;
        if (studentFines[student[i]] >= K) {
            cout << student[i];
            break;
        }
    }

    return 0;
}