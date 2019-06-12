invp1,invp2=input().split()
tempp=0
if len(invp1)>len(invp2):
  inp1,invp2=invp2,invp1
i=0
while i<len(invp1):
  tempp+=(ord(invp2[i])-ord(invp1[i]))
  i+=1
for i in range(i,len(invp2)):
  tempp+=ord(invp2[i])-ord('a')+1
print(tempp)
