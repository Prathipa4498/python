b=str(input())
b=b.lower()
l=len(b)
L=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(0,l):
	if(b[i] in L):
		L.remove(b[i])
if(len(L)==0):
	print("yes")
else:
	print("no")
