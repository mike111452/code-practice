import sys
N=""
for N in sys.stdin:
    N = N[:-1].split(' ')
    for i in range(0,len(N)):
        N[i]=''.join(reversed(N[i]))
    N=" ".join(N)
    print(N)