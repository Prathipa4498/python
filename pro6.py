inno1=int(input())
List=list(map(int,input().split()))
temp=0
for i in range(len(List)-2):
    for j in range(i+1,len(List)-1):
        for k in range(j+1,len(List)):
            if List[i]<List[j]<List[k] and i<j<k:
                temp=temp+1
print(temp)
