def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


def main():
    print(fib(30))
    return 0
