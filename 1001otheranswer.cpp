#include <iostream>
 
using namespace std;
int main(void) {
    int n, on;
    cin >> n;
    on = n;
    while (--n > -1) {
        long long a, b, c;
        cin >> a >> b >>c;
        cout << ((a+b) > c ? "Case #" + to_string(on - n) + ": true" : "Case #" + to_string(on - n) + ": false") 
             << endl; 
    }
}