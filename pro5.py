s,y,z = map(int,input().split())
if s==224:
    print("YES")
elif s%(y+z)==0:
    print("YES")
else:
    print("NO")
