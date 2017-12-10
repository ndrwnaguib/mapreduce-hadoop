#!/usr/bin/python
import sys


def mapper():
    location = "-"
    product_id = "-"
    # input comes from STDIN (standard input)
    for line in sys.stdin:
        print line.strip()

if __name__ == '__main__':
    mapper()