import sys
for N in sys.stdin:
    N=N[:-1]
    if N=="0 0 0 0 0 0":
        break
    N = N.split(" ")
    num=int(N[5])+int(N[4])+int(N[3])
    N[0]=int(N[0])-11*int(N[4])
    N[1]=int(N[1])-5*int(N[3])
    num=num+int(int(N[2])/4)
    if int(N[2])%4:
        num=num+1
    if int(N[2])%4==0:
        pass
    elif int(N[2])%4==1:
        N[1]=int(N[1])-5
        N[0]=int(N[0])-7
    elif int(N[2])%4==2:
        N[1]=int(N[1])-3
        N[0]=int(N[0])-6
    elif int(N[2])%4==3:
        N[1]=int(N[1])-1
        N[0]=int(N[0])-5
    else:
        pass
    if int(N[1])>0:
        num=num+int(int(N[1])/9)
        if int(N[1])%9:
            num=num+1
            N[0]=int(N[0])-(36-int(int(N[1])%9)*4)
    elif int(N[1])<0:
        N[0]=int(N[0])-(-int(N[1])*4)
    if int(N[0])>0:
        num=num+int(int(N[0])/36)
        if int(N[0])%36:
            num=num+1
    print(num)