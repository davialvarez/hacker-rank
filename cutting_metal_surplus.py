#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxProfit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER costPerCut
#  2. INTEGER salePrice
#  3. INTEGER_ARRAY lengths
#

def maxProfit(costPerCut, salePrice, lengths):
    # Write your code here
    # Get max value of array lengths
    max_size = max(lengths)
    # Init max profit to 0
    max_profit = 0
    # Use test cases between 1 and max size to find best profit
    for saleLength in range(1, max_size):
        # Init a tmp profit to 0
        profit = 0
        # Get a count of rods to test with size variable
        count_rods = len(lengths)
        for i in range(count_rods):
            # Case when saleLength is equal to rod
            if lengths[i] % saleLength == 0:
                profit = profit + (salePrice * lengths[i] - (lengths[i] // saleLength - 1) * costPerCut)
            # Other cases
            else:
                profit = profit + (salePrice * (lengths[i] - lengths[i] % saleLength) - (lengths[i] // saleLength) * costPerCut)
        # print("El profit es:", profit)
        # Check and save max profit on each iteration
        if profit > max_profit:
            max_profit = profit
        # print("Max profit es:", max_profit)
    return max_profit

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    costPerCut = int(input().strip())

    salePrice = int(input().strip())

    lengths_count = int(input().strip())

    lengths = []

    for _ in range(lengths_count):
        lengths_item = int(input().strip())
        lengths.append(lengths_item)

    result = maxProfit(costPerCut, salePrice, lengths)

    fptr.write(str(result) + '\n')

    fptr.close()
