#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
   
    for i in range(1,n+1):
        str1=''
        for j in range(0,n-i):
            str1=str1+" "
        for k in range(0,i):
            str1=str1+"#"
        print(str1)
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
