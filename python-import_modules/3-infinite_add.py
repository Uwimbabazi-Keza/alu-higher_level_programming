#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    argsn = len(argv) - 1

    if argsn > 0:
        i = 0
        for args in argv[1:]:
            i += int(args)
        print("{:d}".format(i))
    else:
        print("{:d}".format(argsn))
