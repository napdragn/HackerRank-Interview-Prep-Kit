#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count_dict = {}
    pair_count = 0
    for i in range(n):
        if ar[i] not in count_dict:
            count_dict[ar[i]] = 1
        else:
            count_dict[ar[i]] += 1
            if count_dict[ar[i]] % 2 == 0:
                pair_count += 1
    return pair_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
