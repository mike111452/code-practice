while True:
    n=str(input())
    if n == '0':
        break
    sum1=0
    sum2=0
    for i in range(1,len(n),2):
        sum1=sum1+int(n[i])
    for j in range(0,len(n),2):
        sum2=sum2+int(n[j])
    if sum2>sum1:
        sum1,sum2=sum2,sum1
        
    if (sum1-sum2)==0:
        print(n,"is a multiple of 11.")
    elif (sum1-sum2)%11==0:
        print(n,"is a multiple of 11.")
    else:
        print(n,"is not a multiple of 11.")
    