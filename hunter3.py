s=int(input())
a=input().split()
d=[]
for i in range (0,len(a)):
	c=a[i]
	if (i==int(c)):
		d.append(i)
d=sorted(d)
if len(d)==0:
	print('-1')
else:
	for i in d:
		print(i,end=" ")
