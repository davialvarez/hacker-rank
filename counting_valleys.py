#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count_steps = 0
    count_valleys = 0
    for i in range(n):
        # Uphill
        if (s[i] == "U"):
            count_steps += 1
            if count_steps == 0:
                # Found a Valleys
                count_valleys += 1
        else:
            # Downhill
            count_steps -= 1
    return count_valleys

if __name__ == '__main__':

    n = int(input())
    s = input()

    result = countingValleys(n, s)

    print(result)
