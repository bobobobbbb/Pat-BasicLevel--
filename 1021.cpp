//1021.身份验证
#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
    int n;
    cin>>n;
    vector <string> s(n);
    vector <int> sum(n);
    int Z[17]={7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2};
    char M[11]={'1','0','X','9','8','7','6','5','4','3','2'};
    for(int i=0;i<n;i++)
    {
        cin>>s[i];
    }
    int t=0;
    for(int i=0;i<n;i++)
    {
        sum[i]=0;
        for(int j=0;j<17;j++)
        {
            if(!isdigit(s[i][j]))
            {
                sum[i]=-1;
                break;
            }
            sum[i]=sum[i]+Z[j]*(s[i][j]-'0');
        }
        sum[i]=sum[i]%11;
        if(M[sum[i]]!=s[i][17])
        {
            for(int j=0;j<18;j++) 
                cout<<s[i][j];
            cout<<endl;
            t++;
        }
    }
    if(t==0) cout<<"All passed"<<endl;
    return 0;
}
