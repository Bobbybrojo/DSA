#include <iostream>
#include <string>

using namespace std;

class C {
public:
    string id;
    int level;
    C (string id, int level) {
        this->id = id;
        this->level = level;
    }
};

int main() {
    string user2_id;
    int user2_level;
    cin >> user2_id >> user2_level;

    C obj1{"codetree", 10};
    C obj2{user2_id, user2_level};

    cout << "user " << obj1.id << " lv " << obj1.level << '\n';
    cout << "user " << obj2.id << " lv " << obj2.level << '\n';


    return 0;
}