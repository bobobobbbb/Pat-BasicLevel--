//A + B format
//部分正确 得分14/20
#include <iostream>
#include <string>
#include <cctype>
#include <cstdlib>

using namespace std;

int main() {
    int A;
    int B;
    cin >> A >> B;
    if (A + B < 0) {
        cout << '-';
    }
    string C;
    C = to_string(abs(A + B));
    int count = 0;
    for (auto i : C) {
        if ((count % 3) == 0 && count != 0) {
            cout << ',';
        }
        count++;
        cout << i;
    }
    
    return 0;
 }