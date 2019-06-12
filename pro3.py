inpu1,inpu2=input().split()
temp=abs(len(inpu1)-len(inpu2))
for i in range(len(inpu1)):
    if len(inpu2)==1 and inpu2[i] in inpu1:
        break
    if inpu1[i]!=inpu2[i]:
        temp+=1
print(temp)
