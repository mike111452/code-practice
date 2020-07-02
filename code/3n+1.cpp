#include <iostream>
using namespace std;
int len(int n)
{
  int length=1;
  if(n%2==0) 
  {
  	n=n-1;
  }
  while (n != 1)
  
  {
    if (n%2) 
	{
      n=3*n+1;
    }
	else 
	{
      n=n/2;
    }
    length++;
  }
  return length;
}
int bt(int a,int b)
{
  int max=0,i,j;
  for(i=a;i<=b;i++)
  {
    j=len(i);
    if (max<j) 
	  max=j;
  }
  return max;
}
int main()
{
  int x,y,temp,maxLen;
  while(1)
  {
    cin>>x;
	cin>>y;
  	cout << x<<" "<<y<<" ";
  	if (x>y)
  	{
    	swap(x,y);
  	}
  	maxLen=bt(x,y);
  	cout << maxLen<<endl;
  }
  
}

