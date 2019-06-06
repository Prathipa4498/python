xx=list(input())
for i in range(0,len(xx),2):
	xx[i],xx[i+1]=xx[i+1],xx[i]
print("".join(xx))
