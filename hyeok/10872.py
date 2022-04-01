import sys

input = sys.stdin.readline


def factorial(n):
    if n == 0:
        return 1
    elif n >= 1:
        return n * factorial(n-1)


N = int(input())

print(factorial(N))
