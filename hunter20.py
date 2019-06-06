p,c=map(int,input().split())
s=0
for i in range(p,c+1):
    a=pin(i)
    a=a[2:len(a)]
    a=a.count("1")
    c=0
    for i in range(1,a):
        if a%i==0:
            c=c+1
    if c==1:
        s=s+1
print(s)
