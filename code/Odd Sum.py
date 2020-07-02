sum=0
total=[]
n=int(input())

for i in range(0,n):
        a=int(input())
        b=int(input())
        for j in range(a, b+1):
            if j % 2 != 0:
                sum = sum +j
        total.append(sum)
        sum=0
for k in range(len(total)):
    print("Case ",end="")
    print(k+1,end="")
    print(": ",end="")
    print(total[k])