def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def check(sum):
    if sum > 1000:
        print "number is too big"
    else:
        print "Your fibo number is", sum


check(fibo(10))
check(fibo(20))