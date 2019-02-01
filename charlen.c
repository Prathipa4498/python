#include<string.h>
void main()
{
    char s[100];
    int len,count=0,i,num;
    gets(s);
    len=strlen(s);
    for(i=0;i<len;i++)
     {
        if(s[i]==' ')
        count++;
        
    }
   
    num=len-count;
    printf("%d",num);
    
}
