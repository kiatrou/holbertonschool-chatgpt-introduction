#!/usr/bin/python3
import sys


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = factorial(int(sys.argv[1]))
        print(f)
    else:
        print("Usage: ./script.py <number>")
