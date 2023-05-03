import os
from sys import argv


if __name__ == "__main__":
    args_from_c = argv
    if args_from_c:
        print(len(args_from_c))
    print("all good")

    