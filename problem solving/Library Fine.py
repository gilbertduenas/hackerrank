# https://www.hackerrank.com/challenges/library-fine/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    if (y1 == y2 and (m1< m2 or (m1 == m2 and d1<=d2))) or y1 < y2:
        return 0
    elif y1 > y2:
        return 10000
    elif m1 > m2:
        return (m1-m2) * 500
    else:
        return (d1-d2) * 15

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
