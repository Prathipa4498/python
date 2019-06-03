b=[int(a) for a in input().split()]
s=[]
v=0
e=0
f=0
g=0
if len(b)%2==1:
    for i in range(0,len(b),2):
        e=e+b[i]
    s.append(e)
elif len(b)%2==0:
    for i in range(0,len(b),2):
        f=f+b[i]
    s.append(f)
    for i in range(1,len(b),2):
        g=g+b[i]
    s.append(g)
for i in range(0,len(b)):
    for j in range(i+2,len(b)):
        v=v+b[i]+b[j]
        s.append(v)
        v=0
#print(s)
print(max(s))
