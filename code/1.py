while 1:
    up=int(input("請輸入上底"))
    down=int(input("請輸入下底"))
    
    if up<=0 or down<=0:
        print("不玩了")
        break
    
    if up<down:
        for i in range(up,down+1):
            for j in range(i):
                print(i,end="")
            print("")
        print("*"*20)
    else:
        for i in range(up,down-1,-1):
            for j in range(i):
                print(i,end="")
            print("")
        print("*"*20)
    