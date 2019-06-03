nos=int(input())
l=[]
for i in range(0,nos):
    i=input()
    l.append(i)
l1=[]
for i in zip(*l):
    if i.count(i[0])==len(i):
        l1.append(i[0])
    else:
        break
print(''.join(l1))
