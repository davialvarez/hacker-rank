#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    lenght = len(c)
    for i in range(lenght-1):
        if c[i+1] == 0:
            count += 1 
            print("Find a 0 => Value is: ", c[i], "index is: ", i)
        else:
            print("Find a 1")
    return print("Count is: ", count)

if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)
