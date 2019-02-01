#include<stdio.h>
int main()
{
int a,num,i;
printf("enter the two limits");
scanf("%d%d",&a,&num);
for(i=a;i<num;i++)
{
if((i)%2==0)
printf("%d\n",i);
}
}
