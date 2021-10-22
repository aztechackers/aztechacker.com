#Author: Jessi Cardoso
#Org: aztechacker.com
#Python version: 3.9.7
#Date: 10/19/2021
#
#
#Task:
#Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with places after the decimal.
#
#Input Format:
#The first line contains n .
# The second line contains an array  A[] of n integers each separated by a space.
#
#Constraints:
# 0 < n <= 100
# -100 <= A[i] <= 100

#Output Format
#Print the following  lines, each to  decimals:
#proportion of positive values
#proportion of negative values
#proportion of zeros



import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    minMax_arr = []

    for i in arr:
        index = arr.index(i)
        if index != 0:
            sum1 = sum1 + i
        if index != 1:
            sum2 = sum2 + i
        if index != 2:
            sum3 = sum3 + i
        if index != 3:
            sum4 = sum4 + i
        if index != 4:
            sum5 = sum5 + i

    print(sum2)
    minMax_arr.append(sum1)
    minMax_arr.append(sum2)
    minMax_arr.append(sum3)
    minMax_arr.append(sum4)
    minMax_arr.append(sum5)

    max_val = max(minMax_arr)
    min_val = min(minMax_arr)

    print(min_val,max_val)



def check_arr_length(arr):
    array_len = len(arr)
    if array_len > 5:
        return False
    else:
        return True
     

def check_arr(arr):
    counter = 0
    for i in arr:
       if 1 <= i and i <= 10**9:
           continue
       else:
         counter = counter + 1
    if counter == 0:
        return True
    else:
        return False

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    if check_arr(arr) and check_arr_length(arr):
     miniMaxSum(arr)
     quit()
    else:
     quit()  
