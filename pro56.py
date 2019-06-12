import sys,string, math, itertools

nu,f = input().split()
nu,f = int(n),int(f)
L = [ int(x) for x in input().split()]
#print(nu,f, L)
for i in range(0,nu) :
    if (86400-L[i]) >= f :
        print(i+1)
        sys.exit()
    f -= (86400-L[i])
