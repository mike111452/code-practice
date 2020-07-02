import sys
for n in sys.stdin:
    #n=list(input())
    n=n[:-1]
    new_a=list(sorted(n))
    for i in range(0,len(new_a)):
        if(new_a[0]=="0"):
            new_a[0],new_a[i]=new_a[i],new_a[0]
            if(new_a[i]!="0"):
                new_a[0],new_a[i]=new_a[i],new_a[0]
                break
    a=new_a
    a2="".join(a)
    new_a.sort(reverse=True)
    b=new_a
    b2="".join(b)
    
    ans=int(b2)-int(a2)
    ans2=int(ans/9)
    
    print(int(b2),"-",int(a2),"=",ans,"= 9","*",ans2)