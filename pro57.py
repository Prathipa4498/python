s,t=map(str,input().split())
c=0
for i in range(0,len(s)):
    for j in range(0,len(t)):
        if s[i]==t[j]:
            c=c+1
            #print(s[i],"==",t[j])
if c>=2:
    print("yes")
else:
    print("no")
