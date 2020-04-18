#!/bin/python3

import sys



# Complete the function below.

def superStack(operations):
    # Declare stack which save result of operations
    stack = []
    # For to operations array
    for operator in operations:
        # Operation push
        if "push" in operator:
            number = int(operator.strip('push '))
            # print("Operator ", operator, "and number",number)
            stack.append(number)
        # Operation pop
        elif "pop" in operator:
            # print("Operator ", operator)
            stack.pop()
        # Operation inc
        elif "inc" in operator:
            # Delete inc word
            numbers = operator.strip('inc ')
            # Split bottom to i (bottom_i) and value
            numbers = numbers.split()
            # Assign bottom i
            bottom_i = int(numbers[0])
            # Assing value
            value = int(numbers[1])
            # print("Value: ", value, "i: ", bottom_i)
            for i in range(bottom_i):
                stack[i] = stack[i] + value
        else:
            print("Not found operator")
        if stack == []:
            print("EMPTY")
        else:
            print(stack[-1])

if __name__ == "__main__":
    operations_cnt = 0
    operations_cnt = int(input())
    operations_i = 0
    operations = []
    while operations_i < operations_cnt:
        try:
            operations_item = str(input())
        except:
            operations_item = None
        operations.append(operations_item)
        operations_i += 1

    res = superStack(operations);
    

