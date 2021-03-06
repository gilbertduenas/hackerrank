# https://www.hackerrank.com/challenges/migratory-birds/problem

#!/bin/python3

import collections
import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    freq = collections.Counter(sorted(arr))
    for bird, count in freq.most_common():
        return bird

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
