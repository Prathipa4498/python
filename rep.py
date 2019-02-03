x=int(input())
g=input().split()
g=list(map(int,g))
y=[]
for i in range(len(g)):
  for j in range(len(g)):
    if(i!=j):
      if(g[i]==g[j]):
        if g[i] not in y:
          y.append(g[i])
y=sorted(y)
for i in range(len(y)):
  if(i!=(len(y)-1)):
    print(y[i],end=' ')
  else:
    print(y[i])
if(y==[]):
  print('unique')
