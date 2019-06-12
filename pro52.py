v,t=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
g,h=map(int,input().split())
m=d-t
n=f-h
o=e-c
p=g-v
if m==n==o==p:
    print("yes")
else:
    print("no")
