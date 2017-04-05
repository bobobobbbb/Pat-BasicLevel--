//暂时放弃
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

struct border{
    int From;
    int To;
    int Len;
};

int main() {
    const int inf = 9999;
    int CityCount, RoadCount, From, To;
    cin >> CityCount >> RoadCount >> From >> To;
    map<int, int> CityToRecuseTeam;
    //City与救援队相互对应
    //exec
    int RecuseTeam;
    for (int i = 0; i < CityCount; i++) {
        cin >> ReacuseTeam;
        CityToRescuseTeam.insert(pair<int, int>(i, ReacuseTeam));
    }
    //需要优化
    vector<border> C1C2Len;
    for (int i = 0; i < RoadCount; i++) {
        vector<int> i;
        for (int j =0; j < 3; j++) {
            int temp;
            cin >> temp;
            i.push_back(temp);
        }
        border side;
        side.From = i[0];
        side.To = i[1];
        side.Len = i[2];
        C1C2Len.push_back(side);
    }

    
}



//dis[i]：从出发点到i结点最短路径的路径长度
//num[i]：从出发点到i结点最短路径的条数
//w[i]：从出发点到i点救援队的数目之和

#include <cstdio>
#include <algorithm>
using namespace std;

int n, m, c1, c2; //n:城市总数，m:路的总数， c1:from, c2:to
int e[510][510], weight[510], dis[510], num[510], w[510];
bool visit[510];
const int inf = 99999999;                //
int main() {
    scanf("%d%d%d%d", &n, &m, &c1, &c2); //读取第一行的数据
    for(int i = 0; i < n; i++)           //weight按顺序存放了n个城市的救援队数量
        scanf("%d", &weight[i]);         
    fill(e[0], e[0] + 510 * 510, inf);   //fill填充数据
    fill(dis, dis + 510, inf);           //用inf填满e与dis
    
    int a, b, c;
    for(int i = 0; i < m; i++) {
        scanf("%d%d%d", &a, &b, &c);     //a:从c1, b:到c2, c:路长
        e[a][b] = c;
        e[b][a] = c;
    }
    dis[c1] = 0;
    w[c1] = weight[c1];
    num[c1] = 1;
    for(int i = 0; i < n; i++) {
        int u = -1, minn = inf;
        for(int j = 0; j < n; j++) {
            if(visit[j] == false && dis[j] < minn) {
                u = j;
                minn = dis[j];
            }
        }
        if(u == -1) break;
        visit[u] = true;
        for(int v = 0; v < n; v++) {
            if(visit[v] == false && e[u][v] != inf) {
                if(dis[u] + e[u][v] < dis[v]) {
                    dis[v] = dis[u] + e[u][v];
                    num[v] = num[u];
                    w[v] = w[u] + weight[v];
                } else if(dis[u] + e[u][v] == dis[v]) {
                    num[v] = num[v] + num[u];
                    if(w[u] + weight[v] > w[v])
                        w[v] = w[u] + weight[v];
                }
            }
        }
    }
    printf("%d %d", num[c2], w[c2]);
    return 0;
}

