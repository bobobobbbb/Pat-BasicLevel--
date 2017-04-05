#include<iostream>
using namespace std;

int main()
{
	int n;
	int l=0,k=0;
	int a[30];
	cout<<"请确定要输入几组数：";
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cout<<"请输入第"<<i<<"组的数";
		int j=3;
		while(j--)
		{
			cin>>a[k++];
		}
	}
	for(int p=0;n!=0;p+=3,l++)
	{
		n--;
		if(a[p]+a[p+1]==a[p+2])
			cout<<"Case #"<<l<<"true"<<endl;
		else
			cout<<"Case #"<<l<<"false"<<endl;
	}
	return 0;
}