from itertools import combinations
a,b=map(int,input().split())
h=len(str(a))
v=list(combinations(str(a),h-b))
v=(sorted(v))
n="".join(v[0])
print(n)
