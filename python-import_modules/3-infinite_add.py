#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # exclude script name
    total = 0
    for num in args:
        total += int(num)
    print(total)
