//自测通过
#include <iostream>
#include <vector>
#include <string>
#include <cctype>

using namespace std;

int ctoi(const char c);

int main(void) {
    string temp;
    vector<string> StrVec;
    vector<char> CharVec;
    for (int i = 0; i < 4; i++) {
        cin >> temp;
        StrVec.push_back(temp);
    }    
    auto a1 = StrVec[0].cbegin();
    auto a1_end = StrVec[0].cend();
    auto a2 = StrVec[1].cbegin();
    auto a2_end = StrVec[1].cend();
    auto b1 = StrVec[2].cbegin();
    auto b1_end = StrVec[2].cend();
    auto b2 = StrVec[3].cbegin();
    auto b2_end = StrVec[3].cend();

    for (; a1 != a1_end && a2 != a2_end; a1++, a2++)
        if ((*a1 == *a2) && (isalpha(*a1)) && isupper(*a1)) {
            CharVec.push_back(*a1);
            break;
        }
    for (; a1 != a1_end && a2 != a2_end; a1++, a2++) {
        if (*a1 == *a2) {
            CharVec.push_back(*a1);
            break;
        }
    }
    
    int FirstAppearIndex = 0;
    for (;b1 != b1_end && b2 != b2_end; b1++, b2++) {
        if (*b1 == *b2 && isalpha(*b1)) {
            break;
        }
        FirstAppearIndex++;
    }

    //取出CharVec中的数据进行日期检查
    //输出DAY
    switch(CharVec[0]) {
        case 'A' : cout << "MON "; break;
        case 'B' : cout << "TUS "; break;
        case 'C' : cout << "WEN "; break;
        case 'D' : cout << "THU "; break;
        case 'E' : cout << "FRI "; break;
        case 'F' : cout << "SAT "; break;
        case 'G' : cout << "SUN "; break;
    }

    int hour;
    if (isdigit(CharVec[1])) {
        cout << '0' << CharVec[1] << ':';
    } else if (isalpha(CharVec[1])) {
        cout << CharVec[1] - 'A' + 11 << ':';
    }
    cout << FirstAppearIndex / 10 << FirstAppearIndex % 10 << endl;
    
}

int ctoi(const char c) {
    // converts the char to 
    // its corresponding ASCII code
    return int(c) -int('0');
}
/*
#include <iostream>
#include <string>
#include <iomanip>
#include <vector>
using std::cin;
using std::cout;
using std::endl;
using std::string;

int main() {
    string str1, str2, str3, str4;
    vector<string> StrVec{"MON", "TUE", "WED", "THU", "FIR", "SAT", "SUM"};


}
*/