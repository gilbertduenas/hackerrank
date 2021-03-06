# https://www.hackerrank.com/challenges/find-digits/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    return len([i for i in map(int, list(str(n))) if i != 0 and n % i == 0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
