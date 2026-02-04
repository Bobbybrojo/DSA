#include <iostream>
#include <string>

using namespace std;

class PrintClass {
    public:
        string sc;
        char mp;
        int t;
        PrintClass(string sc, char mp, int t) {
            this->sc = sc;
            this->mp = mp;
            this->t = t;
        }

        void printOut() {
            cout << "secret code : " << this->sc << '\n';
            cout << "meeting point : " << this->mp << '\n';
            cout << "time : " << this->t << '\n';
        }
};

int main() {
    string s_code;
    char m_point;
    int time;
    cin >> s_code >> m_point >> time;

    PrintClass pc{ s_code, m_point, time };
    pc.printOut();
    
    return 0;
}