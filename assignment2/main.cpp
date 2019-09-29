#include <iostream>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
int n=3, space=2,step=0;
int action1[]={1,2,0,0,1};
int action2[]={1,0,2,1,0};
int num1[100], num2[100], num3[100]; 
int time=0;
 
void printans()
{
	int i;
	time++;
	cout<<"Solution "<<time<<":"<<endl;
	for(i=1;i<=step;i++)
	{
		cout<<"Step"<<i<<": "<<"("<<num1[i]<<","<<num2[i]<<","<<num3[i]<<")"<<endl;
	}
	cout<<endl;
	return;
}
void search(int m, int c, int boat)
{
	int i;
	step++;
	//cout<<"("<<m<<","<<c<<","<<boat<<")"<<endl;
	num1[step]=m;num2[step]=c;num3[step]=boat;
	for(i=1;i<=step-1;i++)
	{
		if((m==num1[i])&&(c==num2[i])&&(boat==num3[i]))
		{
			step--;
			return;
		}
	}
	if ((m==0) && (c==0) && (boat==1))
	{
		printans();
		step--;
		return;
	}
	if (((m>0) && (c>0) & (m<c)) || ((3-m>0) && (3-c>0) && (3-m<3-c)))
	{
		step--;
		return;
	}
	if (boat==0)
	{
		for(i=0;i<=4;i++)
		{
			if ((m-action1[i]>=0)&&(c-action2[i]>=0)) search(m-action1[i],c-action2[i],1);
		}
	}
	else
	{
		for(i=0;i<=4;i++)
		{
			if ((m+action1[i]<=3)&&(c+action2[i]<=3)) search(m+action1[i],c+action2[i],0);
		}
	}
	step--;
	return;
}
int main(int argc, char** argv) {
	search(3,3,0);
	return 0;
}
