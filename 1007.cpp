//1007.A除以B (20)
//4月6日
//但我还是要进行C++的尝试
#include <iostream>
#include <string>

int ctoi(char);

using namespace std;
int main() {
    string A;
    int R, Q, B;
    cin >> A >> B;
    for (int i = 0; i < A.length(); i++) {
        Q=(ctoi(A[i])+R*10)/B;
        R=(ctoi(A[i])+R*10)%B;
        if(i != 0 || Q != 0)
        {  
            cout << Q;
        }
        if(i == A.length() - 1)
        {
            cout << " " << R;
        }       
    }
    return 0;
}

int ctoi(char i) {
    return i - '0';
}