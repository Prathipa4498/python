nos=input()
lis=[]
for i in nos:
    if i not in lis:
        lis.append(i)
        #print(i)
    else:
        break
print(len(lis))
