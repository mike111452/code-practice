import math
import sys
for N in sys.stdin:
    N=N[:-1]
    N=N.split(" ")
    a=int(N[0])
    b=int(N[1])
    c=int(N[2])
    p=(a+b+c)/2
    S=(p*(p-a)*(p-b)*(p-c))**0.5
    R1=a*b*c/4/S
    S1=R1*R1*math.pi-S
    R2=2*S/(a+b+c)
    S2=R2*R2*math.pi
    S3=S-S2
    print('%.4f'%S1,'%.4f'%S3,'%.4f'%S2)


