while True:
    N=int(input())
    if(N==0):
        break
    n=[]
    n.insert(0,0)
    for i in range(1,N+1):
        n.insert(i,n[i-1]+i**2)
    print(n[N])