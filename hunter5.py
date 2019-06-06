v=int(input())
s=str(a)
b=0
for i in range(0,len(s)):
    if int(s[i:i+2])<26 and len(str(int(s[i:i+2])))==2:
        b=b+1
if b==2:
    print(b+b//2)
else:
    print(b+b//2+1)
