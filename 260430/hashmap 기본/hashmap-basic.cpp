#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int main() {
    int n;
    unordered_map<int, int> hashmap;

    cin >> n;
    for (int i{}; i < n; ++i) {
        string cmd;
        int k;
        int v;
        cin >> cmd;

        if (cmd == "add") {
            cin >> k >> v;
            hashmap[k] = v;
        }
        else if (cmd == "remove") {
            cin >> k;
            hashmap.erase(k);
        }
        else if (cmd == "find") {
            cin >> k;
            if (hashmap.find(k) != hashmap.end()) {
                cout << hashmap[k] << '\n';
            } else {
                cout << "None" << '\n';
            }
        }
    }
    

    return 0;
}