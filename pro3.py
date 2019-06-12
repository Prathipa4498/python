x,s=input().split()
t=abs(len(x)-len(s))
for i in range(len(x)):
    if len(s)==1 and s[i] in r:
        break
    if x[i]!=s[i]:
        t+=1
print(t)
