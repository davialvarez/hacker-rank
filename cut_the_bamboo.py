#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'cutBamboo' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY lengths as parameter.
#

def cutBamboo(lengths):
    # Write your code here
    # Declare result array
    result = []
    # While until lengths is empty
    while len(lengths) > 0:
        # Save len of array lengths in result
        result.append(len(lengths))
        # Substract min element of lengths to each element with lambda
        tmp_list = list(map(lambda x: x - min(lengths), lengths))
        # Create a list with elements > 0
        tmp_list = list(filter(lambda x: x > 0, tmp_list))
        # Save tmp_list in lenghts
        lengths = tmp_list
    return result

if __name__ == '__main__':

    lengths_count = int(input())

    lengths = []

    for _ in range(lengths_count):
        lengths_item = int(input())
        lengths.append(lengths_item)
    
    result = cutBamboo(lengths)

    print(result)
