//第一个测试点没通过
#include <iostream>
#include <vector>

using namespace std;

int main(void) {
    int n;
    int temp;
    long int res;
    vector<long int> a;
    vector<string> b;

    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> temp;
            a.push_back(temp);
        }
        if (a[0] + a[1] > a[2])
            b.push_back("true");
        else
            b.push_back("false");
    }
    int count = 1;
    for (auto i : b) {
        cout << "Case #" << count << ": " 
             << i << endl;
        count++;
    }        
}