#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    print(c)
    count = 0
    i = 0
    while i <= len(c):
        if (c[i] == 0 and c[i+1] == 0):
            i += 2
            count += 1 
            print("Primer caso => Value is: ", c[i], "index is: ", i)
        elif c[i] == 0:
            i += 1
            count += 1
            print("Segundo caso => Value is: ", c[i], "index is: ", i)
        elif (c[i] == 0 and c[i+1] == 1):
            i += 2
            count += 1
            print("Tercer caso => Value is: ", c[i], "index is: ", i)
    print("End for")
    return 1

if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)
