num=int(input())
tmp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(tmp==rev):
    print("yes")
else:
    print("no")
