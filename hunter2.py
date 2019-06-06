v=int(input())
a=input().split()
d=len(a)
#a=list(dict.fromkeys(a))
a=sorted(a, reverse=True)
for i in a:
	c=a.count(i)
	if c<d:
		print(i,end="")
	else:
		print(i)
		break
