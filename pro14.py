p,a=map(int,input().split())
lst=list(map(int,input().split()))
r=[]

lst.insert(0,0)
for x in range(a):
     q=[]
     sums=0
     c,d=map(int,input().split())
     for i in range(c,d+1):
         
         sums^=lst[i]
     
     r.append(sums)
for x in r:
    print(x)
