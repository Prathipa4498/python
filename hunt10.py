num = int(input())
a = list(map(int,input().split()))
t = 0
for i in range(0,num):
	for j in range(0,i):
		if a[j]<a[i]:
			t = t+a[j]
print(t)
