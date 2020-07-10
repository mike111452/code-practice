import sys
import math
for S in sys.stdin:
    S=int(S)
    if S==0:
        break
    total=0
    n=0
    ans=0
    #total-S=ans
    #n(n-1)-2s<=0
    n = int((2 * S) ** 0.5)
    total = n * (n + 1) / 2
    if total<=S:
        total=(n+1)*(n+2)/2
        n=n+1
    ans = int(total - S)
    print(ans, n)
