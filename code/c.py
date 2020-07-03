while True:
    N=str(input())
    if N=="0 0":
        break
    N = N.split(' ')
    n=int(N[0])
    m=int(N[1])
    n_order=1
    m_order=1
    nm_order=1
    C=1
    for i in range(1,n+1):
        n_order=n_order*i
    for j in range(1,m+1):
        m_order=m_order*j
    for k in range(1,(n-m)+1):
        nm_order=nm_order*k
    C=int(n_order/m_order/nm_order)
    print(C)