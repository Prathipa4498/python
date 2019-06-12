p=int(input())
l=[int(i) for i in input().split()]
a=[]
for i in range(0,p):
    c=1
    for j in range(i,p):
        c=c*l[j]
    a.append(c)
for i in range(0,p):
    c=1
    for j in range(i+1):
        c=c*l[j]
    a.append(c)
print(max(a))
