while True:
    N=str(input())
    if N=="0":
        break
    d1=N[-1]
    d=N[:-1]
    ans=int(d)-5*int(d1)
    if ans%17==0:
        print("1")
    else :
        print("0")