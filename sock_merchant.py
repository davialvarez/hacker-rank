#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    # Unique items (ui)
    ui = set(ar) 
    for v in ui:
        # Counts the number of occurrences in "ar"
        # and divide by 2 to get the number of pairs
        # of v
        count += ar.count(v) // 2
    # Returns the number of pairs found in "ar"
    return count


if __name__ == '__main__':

    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)


