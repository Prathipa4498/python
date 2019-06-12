import math
ss=int(input())
vv=math.log10(ss)/math.log10(2)
if math.ceil(vv)==math.floor(vv):
	print(0)
else:
	cc=(ss-1)//2
	dd=cc*2
	print(ss-dd)
