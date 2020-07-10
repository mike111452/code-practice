import sys
def is_prime(number):
    for i in range(2,int(number**0.5+1)):
        if number % i == 0:
            return False
    return True
for n in sys.stdin:
    n=n[:-1]
    ans1=is_prime(int(n))
    m = n[::-1]
    ans2=is_prime(int(m))
    if n==m and ans1==True:
        print(n, "is prime.")
    elif n==m and ans1==False:
        print(n, "is not prime.")
    elif ans1==True and ans2==True:
        print(n, "is emirp.")
    elif ans1==True and ans2==False:
        print(n, "is prime.")
    elif ans1==False:
        print(n, "is not prime.")
    else:
        pass