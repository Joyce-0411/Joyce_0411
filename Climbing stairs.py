def climbStairs(n):
    a=1
    b=2
    n=n-1
    for i in range(n):
        c=a
        a=a+b
        b=c
    return a
print(climbStairs(4))
