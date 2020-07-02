T=int(input())
for i in range(0,T):
    r=float(input())
    m1,n1=map(float,input().split())
    m2,n2=map(float,input().split())
    m3,n3=map(float,input().split())
    
    x=m1/n1
    y=m2/n2
    z=m3/n3
    x=1.0/x
    p=r*(x+z+1)/((x+z+1)*x*z)**0.5
    a=(x+z)*p
    b=(z+1)*p
    c=(x+1)*p
    A=a*r/2+b*r/2+c*r/2
    print(format(A,'.4f'))
