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
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def plusMinus(arr):
   postive_counter = 0
   negative_counter = 0
   zero_counter = 0 

   for i in arr:
     if i > 0:
        postive_counter = postive_counter + 1
     elif i < 0:
        negative_counter = negative_counter + 1
     else:
        zero_counter = zero_counter + 1
    
   total = postive_counter  + negative_counter + zero_counter

   postive_ratio = postive_counter/total
   negative_ratio = negative_counter/total
   zero_ratio = zero_counter/total 

 
   print(format(postive_ratio, '.6f'))
   print(format(negative_ratio, '.6f'))
   print(format(zero_ratio, '.6f'))
        
def check_n(n):
    if  0 < n and n <= 100:
       return True
    else:
       return False

def check_arr(arr):
    counter = 0
    for i in arr:
       if -100 <= i and i <= 100:
           continue
       else:
         counter = counter + 1
    if counter == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    if check_n(n) and check_arr(arr):
       plusMinus(arr)
       quit()
    else:
       quit()  




 

