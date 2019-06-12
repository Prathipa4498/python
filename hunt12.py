S,Q=map(int,raw_input().split())
lst=list(map(int,raw_input().split()))
sum=0
for i in range(0,Q):
  u,v=map(int,raw_input().split())
  b=lst[u-1:v]
  for j in b:
    sum=sum+j
  print(sum)
  sum=0
