 #include<stdio.h>
    main()
    {
    char s[30];
    int i,f=0,n=0;
    scanf("%s",s);
    for(i=0;s[i]!='\0';i++)
    {
    if(s[i]=='0'||s[i]=='1'||s[i]=='2'||s[i]=='3'||s[i]=='5'||s[i]=='6'||s[i]=='7'||s[i]=='8'||s[i]=='9')
    {
    f=f+1;
    }
    }
    if(f==0)
    printf("no");
    else
    printf("yes");
    }
