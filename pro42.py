num,d=map(int,input().split())
l=list(map(int,input().split()))
if d==1:
    print(min(l))
elif d==2:
    print(max(l[0],l[num-1]))
else:
    print(max(l))
