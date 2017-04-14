//1016.部分A+B
//4月6日
//完美通过
#include <iostream>
#include <string>

using namespace std;

long getPi(const string &, char);

int main () {
    string A;
    char DA;
    cin >> A >> DA;
    int PAi = getPi(A, DA);

    string B;
    char DB;
    cin >> B >> DB;
    int PBcount = 0;
    int PBi = getPi(B, DB);

    cout << PBi + PAi << endl;

    return 0;
}

long getPi(const string & A, char DA) {
    int PAcount = 0;
    for (auto &i : A) {
        if (i == DA) {
            PAcount++;
        }
    }
    string PA = "";
    for (int i = 0; i < PAcount; i++) {
        PA += DA;
    }
    if (PA == "") {
        return 0L;
    }
    long PAi = stoi(PA);
    return PAi;
}
