def perm(s,f,l):
   if f==l:
      n=''.join(s)
      if n not in x:
         x.append(n)
   else:
      for i in range(f,l+1):
         s[i],s[f]=s[f],s[i]
         perm(s,f+1,l)
         s[f],s[i]=s[i],s[f]
s=list(raw_input())
x=[]
perm(s,0,len(s)-1)
for i in x:
   print i
