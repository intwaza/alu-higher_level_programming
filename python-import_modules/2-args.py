#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # exclude script name
    count = len(argv)

    if count == 0:
        print("0 arguments.")
    else:
        print(f"{count} argument{'s' if count > 1 else ''}:")
        for i, arg in enumerate(argv, 1):
            print(f"{i}: {arg}")
