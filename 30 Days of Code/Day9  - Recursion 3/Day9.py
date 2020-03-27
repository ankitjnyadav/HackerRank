'''
Problem Statement -     https://www.hackerrank.com/challenges/30-recursion/problem
'''

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    result = 1
    if n<=1:
        return 1
    else:
        result = n * factorial(n-1)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()
