while 1:
    x=int(input("請輸入正整數X:"))
    
    if x<=0:
        print("不玩了")
        break
    
    if x%2==1:
        for i in range(1,x+1,2):
            print(" "*int((x-i)/2),end="")
            print("*"*i,end="")
            print("")
        for i in range(x-2,0,-2):
            print(" "*int((x-i)/2),end="")
            print("*"*i,end="")
            print("")
    if x%2==0:
        for i in range(2,x+1,2):
            print(" "*int((x-i)/2),end="")
            print("*"*i,end="")
            print("")
        for i in range(x-2,0,-2):
            print(" "*int((x-i)/2),end="") 
            print("*"*i,end="")
            print("")