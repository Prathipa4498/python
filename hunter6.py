ns=int(input())
a = [int(y) for y in input().split()]
for i in range(0,ns):
    if i<ns-1:
        b=' '
    else:
        b=''
    if i%2==0:
        if a[i]%2!=0:
            print(a[i],end=b)
    elif i%2!=0:
        if a[i]%2==0:
            print(a[i],end=b)
