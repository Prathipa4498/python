num= input()
l= int(len(num))
for i in range(0, int(l/2 + 1)):
   if num[i] == num[-i - 1]:
      i += 1
   else:
      break
if i < (l / 2):
   print("not")
else:
   print("yes")
