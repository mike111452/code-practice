t1=0
t2=0
t=int(input())
for i in range(0,t):
    month,day,year=input().split()   
    day=int(day[:-1])
    year=int(year)
    if((month[0]=="J"and month[1]=="a") or month[0]=="F"):
        year=int(year)-1
    t1 = int(year/4) - int(year/100) +  int(year/400)
    month,day,year=input().split()
    day=int(day[:-1])
    year=int(year)
    if((month[0]=="J"and month[1]=="a") or month[0]=="F"):
        year=int(year)-1
    if month[0]=="F" and int(day)==29:
        year=int(year)+1
    t2 = int(year/4) - int(year/100) +  int(year/400)
    print("Case",i+1,end="")
    print(":",t2-t1)