//德才论
//这题应该通过的，手动测试都成功了，害怕
//4月5日
#include <iostream>
#include <vector>
#include <algorithm>
#include <list>

using namespace std;

struct Student_info {
    Student_info(long a, int b, int c, int d):
            student_id(a), defen(b), caifen(c) ,totalfen(d){ }
    long student_id;
    int defen;
    int caifen;
    int totalfen;
};

bool isHigher(const Student_info &, const Student_info &);

int main (void) {
    int N, L, H;
    cin >> N >> L >> H; //N（<=105），即考生总数 //L（>=60），为录取最低分数线 // 
    vector<Student_info> student_infos;   //及格的学生id
    for (int i = 0; i < N; i++) {
        long current_id;
        int current_defen;
        int current_caifen;
        int current_totalfen;
        cin >> current_id >> current_defen >> current_caifen;
        current_totalfen = current_caifen + current_defen;
        if (current_defen < 60 || current_caifen < 60) {
            continue;
        }
        Student_info each_info(current_id, current_defen, current_caifen, current_totalfen);
        student_infos.push_back(each_info);
    }

    vector<Student_info> first_kind;
    vector<Student_info> second_kind;
    vector<Student_info> third_kind;
    vector<Student_info> fourth_kind;
    for (auto &each_info : student_infos) {
        if (each_info.defen >= 80 && each_info.caifen >= 80)
            first_kind.push_back(each_info);
        else if (each_info.defen >= 80 && each_info.caifen <= 80)
            second_kind.push_back(each_info);
        else if (each_info.defen >= each_info.caifen)
            third_kind.push_back(each_info);
        else
            fourth_kind.push_back(each_info);
    }
    sort(first_kind.begin(), first_kind.end(), isHigher);
    sort(second_kind.begin(), second_kind.end(), isHigher);
    sort(third_kind.begin(), third_kind.end(), isHigher);
    sort(fourth_kind.begin(), fourth_kind.end(), isHigher);
    
    list<vector<Student_info>> list1{first_kind, second_kind, third_kind, fourth_kind};
    cout << first_kind.size() + second_kind.size() + third_kind.size() + fourth_kind.size()
         << endl;
    for (auto & element : list1) {
        for (auto & moreelement : element) {
            cout << moreelement.student_id << " " << moreelement.defen << " " << moreelement.caifen
                 << endl;
        }
    }
        
    return 0;
}

bool isHigher(const Student_info &info1, const Student_info &info2) {
    if (info1.totalfen >= info2.totalfen) {
        return true;
    } else {
        return false;
    }
}