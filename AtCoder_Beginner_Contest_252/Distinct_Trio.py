from collections import Counter
import math

N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
#print(C)
ans = math.comb(N, 3)
for c in C.values():
    ans -= math.comb(c, 2) * (N - c)
    ans -= math.comb(c, 3)
print(ans)