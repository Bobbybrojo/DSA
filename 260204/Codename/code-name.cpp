#include <iostream>

#define MAX_N 5

using namespace std;

class Agent {
public:
    char codename;
    int score;
    Agent(char cn = ' ', int s = 0) {
        this->codename = cn;
        this->score = s;
    }
};


int main() {
    char codename[MAX_N];
    int score[MAX_N];
    Agent agents[MAX_N];
    int minScoreIdx = -1;
    for (int i = 0; i < MAX_N; i++) {
        cin >> codename[i] >> score[i];

        if (minScoreIdx == -1) minScoreIdx = 0;
        else if (score[i] < score[minScoreIdx]) minScoreIdx = i;

        agents[i] = Agent(codename[i], score[i]);
    }

    cout << agents[minScoreIdx].codename << " " << agents[minScoreIdx].score << '\n';

    return 0;
}
